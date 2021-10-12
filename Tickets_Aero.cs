using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace TicketsAero{
    public partial class Tickets : Form {
        public Tickets(){
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e){
            string archivo, ciudado, ciudadd, latori, lonori, latdes, londes;
            Dictionary<string, List<string>> ciudadeso = new Dictionary<string, List<string>>();
            Dictionary<string, List<string>> ciudadesd = new Dictionary<string, List<string>>();

            archivo = System.IO.File.ReadAllText("dataset1.csv");

            string[] infor = archivo.Split(new char[] { '\n', '\r', ',' }, StringSplitOptions.RemoveEmptyEntries);

            for (int i = 6; i < infor.Length; i += 6){
                ciudado = infor[i];
                ciudadd = infor[i + 1];
                latori = infor[i + 2];
                lonori = infor[i + 3];
                latdes = infor[i + 4];
                londes = infor[i + 5];

                if (!ciudadeso.ContainsKey(ciudado))
                    ciudadeso.Add(ciudado, new List<string> { latori, lonori });

                if (!ciudadesd.ContainsKey(ciudadd))
                    ciudadesd.Add(ciudadd, new List<string> { latdes, londes });

            }

            string llamada = "https://api.openweathermap.org/data/2.5/weather?lat=";
            string llamada2 = "&lon =";
            string llave = "&appid=";

            foreach (var ciudador in ciudadeso){
                string id = ciudador.Key;
                string latx = (ciudador.Value as List<string>)[0];
                string lonx = (ciudador.Value as List<string>)[1];

                string llamadat = llamada + latx + llamada2 + lonx + llave;
            }

            foreach (var ciudadde in ciudadesd){
                string id = ciudadde.Key;
                string latx = (ciudadde.Value as List<string>)[0];
                string lonx = (ciudadde.Value as List<string>)[1];

                string llamadat = llamada + latx + llamada2 + lonx + llave;
            }

            using (System.Net.WebClient cliente = new System.Net.WebClient())
            {
                // Get the response string from the URL.
                try
                {
                    resultado = cliente.DownloadString(llamadat);
                }
                catch (System.Net.WebException ex)
                {
                    MessageBox.Show(ex.Message + "\n" + ex.StackTrace + "\n" + ex.Source);
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }
    }
}