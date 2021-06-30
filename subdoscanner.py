from termcolor import colored
from pyfiglet import figlet_format

print((colored(figlet_format("SUBDOMAIN SCANNER", font="future_1"), color="red")))
print((colored("-------------------- Coded by Dzaki Althalsyah -------------------- \n", color="blue")))
print((colored("Github: https://github.com/dzakialthalsyah/   ||   Instagram: https://instagram.com/dzakialthalsyah/ \n\n\n", color="cyan")))

# import module requests
import requests

# function untuk scanning subdomain
def subscanner(scan_nama_domain, scan_nama_subdomain):

    print("\n\n\n---------------- Hasil Scan ----------------")

    # looping untuk mendapatkan url
    for subdomain in scan_nama_subdomain:

        # membuat url dengan memasukkan subdomain satu persatu *bruteforce
        url = f"https://{subdomain}.{scan_nama_domain}"

        # memakai syntax try untuk menghindari crash pada program
        try:
        # sending GET request ke url
            requests.get(url)
        # jika setelah mencoba subdomain satu persatu valid kemudian print url nya
            print(f"[+] {url}")

    # jika url nya invalid kemudian lewatkan
        except requests.ConnectionError:
            pass
# function Desc = scan_nama_subdomain in subdomain, subdomain dan scan_nama_domain in url, url got request

# function utama
if __name__ == "__main__":

    # memasukkan nama domain
    nama_dom = input("Masukkan Domain: ")

    # membuka nama list file subdomain nya
    with open("listdomain.ini","r") as file:

        # membaca file nya
        baca = file.read()

        # memakai garis pemisah/spilitlines() function untuk storing list yang string nya terbelah
        sub_dom = baca.splitlines()


# memanggil function untuk memanggil subdo
subscanner(nama_dom, sub_dom)


