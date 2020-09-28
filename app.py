from flask import render_template, Flask, request

app = Flask(__name__)

# Fungsi untuk merender template index.html
@app.route('/')
def index():
    return render_template('index.html')

# Fungsi untuk memfilter data dari templates
@app.route('/' ,methods = ['POST'])
def getData():
    name = request.form['name']
    nip = request.form['nip']
    message = []

    # Memfilter name harus huruf alphabet
    if name.isalpha() == False:
        message = "Username harus huruf alphabet !!!"
        return render_template('index.html',messages=message,rnip=nip)

    # Memfilter huruf besar(uppercase) pada input data "name"
    names = list(name)
    for i in range(len(names)):
        if names[i].isupper():
            ##### Fungsi untuk mengubah huruf besar(uppercase) menjadi huruf kecil(lowercase) #####
            names[i] = names[i].lower() 
            ##############################################################

            ##### Fungsi untuk menghapus huruf besar(uppercase) pada input data "name" #####
            # names[i] = ''  
            ##############################################################

            ##### Fungsi untuk menolak input data  #####
            # message = "Username harus huruf kecil !!!"
            # return render_template('index.html',messages=message,rnip=nip)
            ##############################################################

    Name = ''.join(names)

    # Memfilter NIP harus 8 character
    if (len(nip)!= 8):
        message = "NIP harus 8 karakter !!!"
        return render_template('index.html',messages=message,rname=name)

    return render_template('index.html',messages=message,name=Name,nip=nip)

if __name__ == '__main__':
    app.run(debug=True)

