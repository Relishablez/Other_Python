import qrcode

url = ""
URL = ""

while True:
    url = input("Enter the URL would you like the QR Code to lead to?").lower()
    if "www." in url:
        print("Valid: \"www.\" Check Success")
        if ".co.uk" in url or ".com" in url or ".gov" in url or ".edu" in url:
            print("Valid: Success")
            URL = "https://" + url
            print(URL)
            break
        else:
            print("Doesn't contain a Top-Level Domain.")
    else:
        print ("This is not a valid URL. Please try again.")

qr = qrcode.QRCode(
	version=1,
	box_size=15,
	border=5
)

domain = URL.split(".")

print(domain)

qr.add_data(URL)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('QR_Code_Images/'+domain[1]+".jpg", "JPEG")

print ("QR Code Successfully Created")
