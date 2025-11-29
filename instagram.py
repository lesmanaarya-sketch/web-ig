J=str
I=Exception
F=input
C=print
import instaloader as K,time as E,sys as G,os,requests as N
from sys import stderr as O
from datetime import datetime
B='\x1b[38;2;245;222;179m'
A='\x1b[1;37m'
D='\x1b[0m'
def L():os.system('clear'if os.name=='posix'else'cls')
def M():O.writelines(f"""{B}
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠈⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣁⣀⣀⣠⣤⣤⣤⣤⣤⠤⠤⠤⠤⠤⢤⣤⣤⣤⣽⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⡿⠛⠛⢿⣿⣿
⣿⣿⣿⣿⡿⠋⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡿⠁⣴⢷⡀⢻⣿
⣿⣿⡟⠁⠀⠀⠀⠙⢿⣄⡀⠀⠀⠀⠀⠀⠀⣤⣤⣼⣿⣿⣿⠃⢸⣿⣾⡇⢸⣿
⣿⠟⠛⠛⠳⠶⣦⣄⡀⠙⠻⣦⣄⣀⠀⢀⣼⣏⠙⣿⣿⣿⣿⠀⢻⣿⣿⠃⣸⣿
⣿⠀⠀⠀⠀⠀⠀⠉⠛⠷⣤⡀⠉⠻⣿⣿⣿⣿⡇⣸⣿⣿⣿⣇⠘⠿⠏⣰⣿⣿
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⣤⡈⣿⣿⣿⠁⣿⣿⣿⣿⣿⡇⢀⣾⣿⣿⣿
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⡇⠀⠀⠈⠙⣿⣿⡇⢸⣿⣿⣿⣿
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣧⣀⠀⣀⣴⣿⣿⠇⢸⣿⣿⣿⣿
⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣤⣾⣿⣿⣿⣿     
Holmes gram Frostwolf 
{B}Author: team Code Frostwolf
{A}Owner Contact: t.me/ownFrostWolff
{B}GitHub: https://github.com/H0Xcysecom
{A}============================================================
{D}""")
def Z():
	for C in range(5):G.stdout.write(f"\r{A}MEMUAT {B}|{D}");E.sleep(.1);G.stdout.write(f"\r{A}MEMUAT {B}/{D}");E.sleep(.1);G.stdout.write(f"\r{A}MEMUAT {B}-{D}");E.sleep(.1);G.stdout.write(f"\r{A}MEMUAT {B}\\{D}");E.sleep(.1)
	G.stdout.write('\r'+' '*20+'\r')
def P(url,username):
	try:
		E=N.get(url,stream=True)
		if E.status_code==200:
			F=f"{username}_profile_pic.jpg"
			with open(F,'wb')as G:
				for H in E.iter_content(1024):G.write(H)
			return os.path.abspath(F)
		return
	except I as K:C(f"{A}[ {B}!{A} ] Error mengunduh foto profil: {J(K)}{D}");return
def Q():C(f"\n{A}============================ {B}MENU HOLMES GRAM {A}============================");C(f"{A}[{B}1{A}] {B}Cek Informasi Lengkap Akun");C(f"{A}[{B}2{A}] {B}Cek ID");C(f"{A}[{B}3{A}] {B}Cek Jumlah Postingan");C(f"{A}[{B}4{A}] {B}Cek Bio");C(f"{A}[{B}5{A}] {B}Cek Nama Lengkap");C(f"{A}[{B}6{A}] {B}Cek Jumlah Pengikut & Mengikuti");C(f"{A}[{B}7{A}] {B}Unduh Foto Profil");C(f"{A}[{B}0{A}] {B}Keluar");C(f"{A}============================================================{D}")
def H(username):
	try:F=K.Instaloader();E.sleep(2);G=K.Profile.from_username(F.context,username);return G
	except I as H:C(f"{A}[ {B}!{A} ] Error: {J(H)}{D}");C(f"{A}[ {B}!{A} ] Akun mungkin tidak ada atau diprivate.{D}");return
def R():
	I='%d-%m-%Y';G='Tidak';J=F(f"\n{A}[{B}+{A}] Masukkan Username Target: {B}");E=H(J)
	if not E:return
	C(f"\n{A}======================== {B}NIH INFO DATA IG TARGET WAK {A}========================");C(f"{A}Username              :{B} {E.username}{D}");C(f"{A}Nama Lengkap          :{B} {E.full_name}{D}");C(f"{A}ID                    :{B} {E.userid}{D}");C(f"{A}Bio                   :{B} {E.biography}{D}");C(f"{A}URL Profil            :{B} {E.external_url}{D}");C(f"{A}Akun Private          :{B} {"Ya"if E.is_private else G}{D}");C(f"{A}Akun Bisnis           :{B} {"Ya"if E.is_business_account else G}{D}")
	if E.is_business_account:C(f"{A}Kategori Bisnis       :{B} {E.business_category_name}{D}")
	C(f"{A}Pengikut              :{B} {E.followers}{D}");C(f"{A}Mengikuti             :{B} {E.followees}{D}");C(f"{A}Total Postingan       :{B} {E.mediacount}{D}")
	try:
		if hasattr(E,'joined_date')and E.joined_date:K=E.joined_date.strftime(I);C(f"{A}Tanggal Bergabung      :{B} {K}{D}")
		else:
			for L in E.get_posts():M=L.date.strftime(I);C(f"{A}Perkiraan Bergabung    :{B} {M} (dari postingan pertama){D}");break
	except:C(f"{A}Tanggal Bergabung      :{B} Tidak dapat diakses{D}")
	N=E.profile_pic_url;C(f"{A}URL Foto Profil       :{B} {N}{D}");C(f"{A}============================================================{D}")
def S():
	G=F(f"\n{A}[{B}+{A}] Masukkan Username Target: {B}");E=H(G)
	if not E:return
	C(f"\n{A}============================ {B}ID AKUN {A}============================");C(f"{A}Username: {B}{E.username}{D}");C(f"{A}ID: {B}{E.userid}{D}");C(f"{A}============================================================{D}")
def T():
	G=F(f"\n{A}[{B}+{A}] Masukkan Username Target: {B}");E=H(G)
	if not E:return
	C(f"\n{A}======================= {B}JUMLAH POSTINGAN {A}=======================");C(f"{A}Username: {B}{E.username}{D}");C(f"{A}Jumlah Postingan: {B}{E.mediacount}{D}");C(f"{A}============================================================{D}")
def U():
	G=F(f"\n{A}[{B}+{A}] Masukkan Username Target: {B}");E=H(G)
	if not E:return
	C(f"\n{A}=========================== {B}BIO AKUN {A}===========================");C(f"{A}Username: {B}{E.username}{D}");C(f"{A}Bio: {B}{E.biography}{D}");C(f"{A}============================================================{D}")
def V():
	G=F(f"\n{A}[{B}+{A}] Masukkan Username Target: {B}");E=H(G)
	if not E:return
	C(f"\n{A}======================= {B}NAMA LENGKAP {A}=======================");C(f"{A}Username: {B}{E.username}{D}");C(f"{A}Nama Lengkap: {B}{E.full_name}{D}");C(f"{A}============================================================{D}")
def W():
	G=F(f"\n{A}[{B}+{A}] Masukkan Username Target: {B}");E=H(G)
	if not E:return
	C(f"\n{A}==================== {B}PENGIKUT & MENGIKUTI {A}====================");C(f"{A}Username: {B}{E.username}{D}");C(f"{A}Jumlah Pengikut: {B}{E.followers}{D}");C(f"{A}Jumlah Mengikuti: {B}{E.followees}{D}");C(f"{A}============================================================{D}")
def X():
	E=F(f"\n{A}[{B}+{A}] Masukkan Username Target: {B}");G=H(E)
	if not G:return
	C(f"\n{A}===================== {B}UNDUH FOTO PROFIL {A}=====================");I=G.profile_pic_url;C(f"{A}URL Foto Profil: {B}{I}{D}");K=F(f"{A}Unduh foto profil? (y/n): {B}")
	if K.lower()=='y':
		J=P(I,E)
		if J:C(f"{A}[{B}+{A}] Foto profil berhasil diunduh: {B}{J}{D}")
		else:C(f"{A}[{B}!{A}] Gagal mengunduh foto profil.{D}")
	C(f"{A}============================================================{D}")
def Y():
	try:
		L();M()
		while True:
			Q();E=F(f"\n{A}[{B}+{A}] Pilih menu: {B}")
			if E=='1':R()
			elif E=='2':S()
			elif E=='3':T()
			elif E=='4':U()
			elif E=='5':V()
			elif E=='6':W()
			elif E=='7':X()
			elif E=='0':C(f"\n{A}[{B}+{A}] Terima kasih telah menggunakan OSINTGRAM!{D}");break
			else:C(f"{A}[{B}!{A}] Pilihan tidak valid.{D}")
			F(f"\n{A}[{B}+{A}] Tekan Enter untuk melanjutkan...{D}");L();M()
	except KeyboardInterrupt:C(f"\n\n{A}[{B}!{A}] Program dihentikan oleh pengguna...{D}");G.exit(0)
	except I as H:C(f"\n{A}[{B}!{A}] Error tak terduga: {J(H)}{D}");G.exit(1)
if __name__=='__main__':Y()
