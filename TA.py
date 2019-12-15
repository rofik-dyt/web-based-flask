from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'rental_mobil'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/Rental', methods=['GET','POST'])

def rental():
    cur = mysql.connection.cursor()
    cur.execute("SELECT merek from mobil")

    if request.method == 'POST':
        details = request.form
        name = details['name']
        alamat = details['alamat']
        nohp = details['nohp']
        jenisin = details['jenisin']
        hari = details['hari']

        if jenisin == 'Toyota Yaris' :
            hasil = int(hari) * 200000

            cur2 = mysql.connection.cursor()
            cur2.execute("INSERT INTO penyewa(nama, alamat, nohp, merek) VALUES (%s, %s, %s, %s)",
                         (name, alamat, nohp, jenisin))
            mysql.connection.commit()

            cur2.execute("SELECT id from penyewa ORDER BY id DESC LIMIT 1")
            id = cur2.fetchone()
            cur2.execute("INSERT INTO lama_sewa(id, hari, harga) VALUES (%s, %s, %s)",
                         (id, hari, hasil))
            mysql.connection.commit()

            cur2.close()

            return redirect(url_for('terima'))

        elif jenisin == 'Honda Jazz':
            hasil = int(hari) * 240000

            cur2 = mysql.connection.cursor()
            cur2.execute("INSERT INTO penyewa(nama, alamat, nohp, merek) VALUES (%s, %s, %s, %s)",
                         (name, alamat, nohp, jenisin))
            mysql.connection.commit()

            cur2.execute("SELECT id from penyewa ORDER BY id DESC LIMIT 1")
            id = cur2.fetchone()
            cur2.execute("INSERT INTO lama_sewa(id, hari, harga) VALUES (%s, %s, %s)",
                         (id, hari, hasil))
            mysql.connection.commit()

            cur2.close()

            return redirect(url_for('terima'))

        elif jenisin == 'Daihatsu Xenia':
            hasil = int(hari) * 260000

            cur2 = mysql.connection.cursor()
            cur2.execute("INSERT INTO penyewa(nama, alamat, nohp, merek) VALUES (%s, %s, %s, %s)",
                         (name, alamat, nohp, jenisin))
            mysql.connection.commit()

            cur2.execute("SELECT id from penyewa ORDER BY id DESC LIMIT 1")
            id = cur2.fetchone()
            cur2.execute("INSERT INTO lama_sewa(id, hari, harga) VALUES (%s, %s, %s)",
                         (id, hari, hasil))
            mysql.connection.commit()

            cur2.close()

            return redirect(url_for('terima'))

        elif jenisin == 'Hyundai Tucson':
            hasil = int(hari) * 250000

            cur2 = mysql.connection.cursor()
            cur2.execute("INSERT INTO penyewa(nama, alamat, nohp, merek) VALUES (%s, %s, %s, %s)",
                         (name, alamat, nohp, jenisin))
            mysql.connection.commit()

            cur2.execute("SELECT id from penyewa ORDER BY id DESC LIMIT 1")
            id = cur2.fetchone()
            cur2.execute("INSERT INTO lama_sewa(id, hari, harga) VALUES (%s, %s, %s)",
                         (id, hari, hasil))
            mysql.connection.commit()

            cur2.close()

            return redirect(url_for('terima'))

    return  render_template('rental.html', title='Rental', jenis=cur.fetchall())

@app.route('/terima')
def terima():
    cur = mysql.connection.cursor()
    cur.execute('SELECT penyewa.*, mobil.plat, mobil.warna, mobil.thn_produksi, lama_sewa.hari, lama_sewa.harga '
                'FROM penyewa INNER JOIN mobil ON penyewa.merek = mobil.merek INNER JOIN lama_sewa ON penyewa.id = lama_sewa.id '
                'ORDER BY id DESC LIMIT 1')
    data = cur.fetchall()

    name = data[0][1]
    alamat = data[0][2]
    nohp = str(data[0][3])
    model = data[0][4]
    plat = data[0][5]
    warna = data[0][6]
    thn = str(data[0][7])
    hari = str(data[0][8])
    harga = str(data[0][9])

    return render_template('terima.html',title='Total', name=name, alamat=alamat,
                           nohp=nohp, model=model, harga=harga, plat=plat, warna=warna, thn=thn, hari=hari)

@app.route('/about', methods=['GET','POST'])
def about():
    if request.method == 'POST':

        return redirect(url_for('home'))

    return render_template('about.html', title='about')


if __name__ == '__main__':
    app.run(debug=True)