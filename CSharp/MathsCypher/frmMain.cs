﻿using System;
using System.Collections.Generic;
using System.Data;
using System.Deployment.Application;
using System.Linq;
using System.Windows.Forms;
using MathsCypher.Properties;

namespace MathsCypher
{
    public partial class frmMain : Form
    {
        public frmMain()
        {
            InitializeComponent();
        }

        private Dictionary<char, int> _mappings = new Dictionary<char, int>();
        private Random _random = new Random();

        private void frmMain_Load(object sender, EventArgs e)
        {
            ActiveControl = txtCodedMessageInput;

            this.AddPublishVersion();

            loadSettings();
            populateMappingsList();
            Icon = Resources.APP_ICON;
        }

        private void frmMain_FormClosed(object sender, FormClosedEventArgs e)
        {
            saveSettings();
        }

        private void saveSettings()
        {
            Settings.Default.CodedMessageInput = txtCodedMessageInput.Text;
            Settings.Default.MappingsList = string.Join(";",
                _mappings.Select(mapping => mapping.Key + "=" + mapping.Value).ToArray()
                );
            Settings.Default.MaxDividendValue = getValidMaxDividendValue();
            Settings.Default.MaxFactorValue = getValidMaxFactorValue();
            Settings.Default.Save();
        }

        private int getValidMaxFactorValue()
        {
            var maxFactorValue = txtMaxFactorValue.Text.ConvertToIntegerOrDefault(12);

            return Math.Max(maxFactorValue, 7);
        }

        private int getValidMaxDividendValue()
        {
            var maxDividendValue = txtMaxDividendValue.Text.ConvertToIntegerOrDefault(144);

            return Math.Max(maxDividendValue, 90);
        }

        private void loadSettings()
        {
            setMapping(Settings.Default.MappingsList);
            txtCodedMessageInput.Text = Settings.Default.CodedMessageInput;
            txtMaxDividendValue.Text = Settings.Default.MaxDividendValue.ToString();
            txtMaxFactorValue.Text = Settings.Default.MaxFactorValue.ToString();
        }

        private void setMapping(string mappings)
        {
            if (mappings == "")
                generateDefaultMappings();
            else
                extractMappings(mappings);
        }

        private void extractMappings(string mappings)
        {
            foreach (var mapping in mappings.Split(';'))
            {
                var splitMapping = mapping.Split('=');
                var key = Convert.ToChar(splitMapping[0]);
                var value = Convert.ToInt32(splitMapping[1]);
                _mappings.Add(key, value);
            }
        }

        private void populateMappingsList()
        {
            lvwMappings.Items.Clear();
            foreach (var mapping in _mappings)
            {
                lvwMappings.Items.Add(
                    new ListViewItem(
                        new[] { mapping.Value.ToString(), mapping.Key.ToString() }
                        )
                    );
            }
        }

        private void generateDefaultMappings()
        {
            _mappings.Clear();
            var number = 2;
            for (char letter = 'A'; letter <= 'Z'; letter++)
            {
                while (number.GetFactors().Count < 4)
                    number++;
                
                _mappings.Add(letter, number++);
            }
        }

        private Timer _regenerateTimer = new Timer();

        private void txtCodedMessageInput_TextChanged(object sender, EventArgs e)
        {
            if (_regenerateTimer.Enabled)
                return;

            _regenerateTimer.Interval = 3000;
            _regenerateTimer.Tick += _regenerateTimer_Tick;
            _regenerateTimer.Start();
        }

        private void _regenerateTimer_Tick(object sender, EventArgs e)
        {
            _regenerateTimer.Stop();
            _regenerateTimer.Tick -= _regenerateTimer_Tick;

            regenerate();

            _regenerateTimer.Interval = 50;
            _regenerateTimer.Tick += _regenerateTimer_Tick2;
            _regenerateTimer.Start();
        }

        private void _regenerateTimer_Tick2(object sender, EventArgs e)
        {
            _regenerateTimer.Stop();
            _regenerateTimer.Tick -= _regenerateTimer_Tick2;

            txtCodedMessageInput.Focus();
        }

        private void cmdRegenerate_Click(object sender, EventArgs e)
        {
            regenerate();
        }

        private void regenerate()
        {
            var codedMessage = new CodedMessage(
                txtCodedMessageInput.Text,
                _random,
                _mappings,
                getValidMaxFactorValue(),
                getValidMaxDividendValue()
                );
            var formattedMessage = new HTMLCodedMessage(codedMessage, _mappings);
            var html = formattedMessage.Generate();
            writeHtmlToWebBrowser(html);
        }

        private void writeHtmlToWebBrowser(string html)
        {
            WebBrowser.DocumentText = string.Empty;
            WebBrowser.Parent.Enabled = false; //https://stackoverflow.com/questions/8495857/webbrowser-steals-focus
            WebBrowser.Document.OpenNew(true);
            WebBrowser.Document.Write(html);
            WebBrowser.Refresh();
            WebBrowser.Parent.Enabled = true;
        }


        private void lvwMappings_AfterLabelEdit(object sender, LabelEditEventArgs e)
        {
            if (e.Label == null)
                return;

            int newNumber;
            if (!int.TryParse(e.Label, out newNumber))
            {
                cancelMappingEdit(e, "Expected an integer");
                return;
            }

            ListViewItem listItem = lvwMappings.Items[e.Item];
            if (e.Label == listItem.Text)
                return;

            if (_mappings.Values.Contains(newNumber))
            {
                cancelMappingEdit(e, "Duplicate number");
                return;
            }

            char letter = Convert.ToChar(listItem.SubItems[1].Text);
            _mappings[letter] = newNumber;
            regenerate();
        }

        private static void cancelMappingEdit(LabelEditEventArgs e, string failureMessage)
        {
            MessageBox.Show(failureMessage);
            e.CancelEdit = true;
        }

        private void cmdDefaultMappings_Click(object sender, EventArgs e)
        {
            generateDefaultMappings();
            populateMappingsList();
            regenerate();
        }

        private void cmdJumble_Click(object sender, EventArgs e)
        {
            var valueList = _mappings.Values.ToList().Shuffle();

            _mappings.Clear();
            var index = 0;
            for (char letter = 'A'; letter <= 'Z'; letter++)
            {
                _mappings.Add(letter, valueList[index++]);
            }

            populateMappingsList();
            regenerate();
        }

        private void cmdCopy_Click(object sender, EventArgs e)
        {
            WebBrowser.Document.ExecCommand("SelectAll", true, null);
            WebBrowser.Document.ExecCommand("Copy", true, null);
            WebBrowser.Refresh();
        }

        private void txtMaxFactorValue_Validated(object sender, EventArgs e)
        {
            txtMaxFactorValue.Text = getValidMaxFactorValue().ToString();
            regenerate();
        }

        private void txtMaxDividendValue_Validated(object sender, EventArgs e)
        {
            txtMaxDividendValue.Text = getValidMaxDividendValue().ToString();
            regenerate();
        }
    }
}