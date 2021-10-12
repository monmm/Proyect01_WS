using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//MOCKUP CODE UTILIZANDO C++ PARA DARNOS UNA IDEA DE LO QUE QUEREMOS HACER/PODEMOS HACER CON EL CÓDIGO

namespace edoTiempoSem3
{
    public partial class edoTiempo : Form
    {
        string ciudades { get; set; }
        string serweb = "https://api.openweathermap.org/data/2.5/weather?q=";
        string unidad = "&units=metric";
        string llave = "&appid=a611c17040f43a736dc5b58ccf972271";
        public edoTiempo()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ciudades = File.ReadAllText("ciudades.txt");

            string[] lciudades = ciudades.Split(new char[] { '\n' }, StringSplitOptions.RemoveEmptyEntries);

            foreach(string ciudad in lciudades)
            {
                l_origen.Items.Add(ciudad);
                l_destino.Items.Add(ciudad);
            }


        }

        private void button1_Click(object sender, EventArgs e)
        {
            string corigen, cdestino,rorigen,rdestino;

            corigen = l_origen.SelectedItem.ToString().Trim();
            cdestino = l_destino.SelectedItem.ToString().Trim();

            if(string.IsNullOrEmpty(corigen)||string.IsNullOrEmpty(cdestino))
            {
                MessageBox.Show("No se ha seleccionado ciudad de origen y/o destino. No continuará la ejecución.");
                return;
            }

            if(corigen.Equals(cdestino))
            {
                MessageBox.Show("Las ciudades de origen y destino son iguales. No continuará la ejecución.");
                return;
            }

            regresaLlamada(corigen, out rorigen);
            regresaLlamada(cdestino, out rdestino);

            txt_resultado.Text = rorigen + "\r\n" + rdestino;
        }

        void regresaLlamada(string ciudad,out string resultado)
        {
            string llamada;

            resultado = string.Empty;
            llamada = serweb + ciudad + unidad + llave;

            using (System.Net.WebClient cliente = new System.Net.WebClient())
            {
                // Get the response string from the URL.
                try
                {
                    resultado = cliente.DownloadString(llamada);
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
