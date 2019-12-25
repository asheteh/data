def Teri_Deewani_Kailash_Kher_Harmonium_Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =1)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bahut_Pyaar_Karte_Hain_Tumko_Sanam_Notes_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =2)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bahut_Pyar_Karte_Hain_Tumko_Sanam_Harmonium_Sargam__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =3)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bahut_Pyar_Karte_Hain_Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =4)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Itna_Na_Mujhse_Tu_Pyar_Badha_Piano_Notes_in_Hindi__Harmonium_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =5)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Deewani_Kailash_Kher_Piano_Notes_in_CDF_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =6)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aye_Mere_Humsafar_Ek_Zara_Intezaar_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =7)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaye_Ho_Meri_Zindagi_Mein__Raja_Hindustani__Notes_Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =8)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Didi_Tera_Devar_Deewana_Sargam__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =9)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phoolon_Sa_Chehera_Tera_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =10)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darde_Dil_Darde_Jigar__Karz__Piano_Notes_in_Hindi__Harmonium_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =11)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Moh_Moh_Ke_Dhaage_Song_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =12)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kajra_Mohabbat_Wala_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =14)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Ke_Jharoke_Mein_Piano_Notes_in_Hindi__Harmonium_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =15)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Mehboob_Qayamat_Hogi_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =17)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Abhi_Mujh_Mein_Kahin__Sonu_Nigam__Harmonium_Notes__Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =19)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Janam_Janam__Arijit_Singh__Piano_Notes__Notations_in_English___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =20)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Abhi_Mujh_Mein_Kahin_Piano_Notes_in_CDF_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =22)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Tere_Shahar_Mein_Aaye_Hain__Ghazal__Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =23)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mera_Piya_Ghar_Aaya_Song_Harmonium_Notes__Sargam_in_Hindi__Piano____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =24)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lag_Jaa_Gale_Song_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =25)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Sapno_Ki_Rani_Kab_Aayegi_Tu_Harmonium_Sagam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =26)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saat_Samundar_Paar_Main_Tere_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =27)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Mitti__Kesari__Song_Harmonium_Sargam__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =28)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaun_Tujhe__MS_Dhoni__Harmonium_Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =29)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumhe_Dillagi_Bhool_Jani_Padegi_Harmonium_Sargam__Piano_Notes_in_Hindi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =30)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaun_Tujhe__MS_Dhoni__Piano_Notes__Notations_with_Lyrics___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =31)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Likhe_Jo_Khat_Tujhe_Harmonium_Sargam___Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =34)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baharon_Phool_Barsao_Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =35)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehla_Nasha_Pehla_Khumar_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =37)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zindagi_Ek_Safar_Hai_Suhana_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =38)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ghar_Aaya_Mera_Pardesi_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =39)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Apna_Aur_Preet_Parai_Song_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =40)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Apni_to_Jaise_Taise_Song_Piano_Notes__Notations____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =41)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Neele_Neele_Ambar_Par_song_Piano_Notes_in_Hindi__Harmonium_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =43)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sandese_Aate_Hain_Piano_Notes_in_Sa_re_ga_ma___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =45)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ajeeb_Dastan_Hai_Yeh_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =46)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Saamne_Wale_Khidki_Song_Sargam__Notations_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =47)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phoolon_Sa_Chehra_Tera_Song_Piano_Notes__CDF_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =49)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Hai_Zameen_Tera_Aasman_Harmonium_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =52)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Cheez_Badi_Hai_Mast_Mast_Sargam__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =53)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Shayar_To_Nahin_Harmoinim_Notes__Sargam_in_Hindi_for_Piano___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =55)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Rashke_Qamar__Baadshaho__Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =59)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Apni_To_Jaise_Taise__Housefull__O_Dhanno_Sargam_Notes_for_Harmonium_Piano___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =60)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Pardesi_Mera_Dil_Le_Gaya_Harmonium_Sargam__Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =61)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Ke_Armaan_Aansuon_Mein_Beh_Gaye_Notes_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =62)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Rashke_Qamar_Piano_Keyboard_Notations__CDF_Notes____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =63)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanam_Re_Full_Song_Piano_Notes__Line_by_Line_By_Notations_with_Lyrics___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =67)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yeh_Shaam_Mastani_Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =68)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gulabi_Aankhein_Jo_Teri_Dekhi_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =70)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_Reshmi_Zulfein_Ye_Sharbati_Aankhein_Notes_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =72)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Karvaten_Badalte_Rahe_Sari_Raat_Hum_Sargam__Harmonium_Notes_in_Hindi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =75)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Do_Lafzon_Ki_Hai_Dil_Ki_Kahani_Sargam_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =78)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zindagi_Pyar_Ka_Geet_Hai_Sargam_Harmonium__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =79)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Mitti__Kesari__Piano_Notes__Western_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =81)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bahon_Mein_Chale_Aao_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =85)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Bina_Zindagi_Se_Koi_Shikwa_Notes_in_Hindi__Sargam__Piano_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =87)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Hai_Ke_Manta_Nahi_Harmonium_Notes__Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =93)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Purani_Raahon_Se_Koi_Mujhe__Song__Harmonium_Sargam__Notes_Piano___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =94)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Lootne_Wale_Jadugar_Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =95)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Milti_Hai_Zindagi_Mein_Mohabbat_Kabhi_Kabhi_Harmonium_Notes_Notations_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =96)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaun_Disa_Mein_Leke_Piano_Notes_in_Hindi__Harmonium_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =97)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Naseeb_Mein_Tu_Hai_Ke_Nahin_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =99)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabhi_Ram_Banke_Kabhi_Shyam_Banke_Bhajan_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =103)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hey_Ram_Hey_Ram_Bhajan_Sargam_for_Harmonium__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =104)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mile_Ho_Tum_Humko_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =106)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aane_Se_Uske_Aaye_Bahar_Notes_Sargam_in_Hindi_for_Harmonium_and_Piano___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =111)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zindagi_Ki_Na_Toote_Ladi_Harmonium_Sargam__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =113)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Teri_Dushman_Song_Piano_Notes_in_Hindi__Harmonium_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =115)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanwali_Surat_Pe_Mohan_Dil_Deewana_Hogya_Sargam_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =121)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ghanshyam_Teri_Bansi_Harmonium_Sargam__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =122)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pal_Pal_Dil_Ke_Paas_Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =123)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kala_Kala_Kahe_Gujri_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =124)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaarti_Kunj_Bihari_ki_Harmonium_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =125)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Radhe_Radhe_Japo_Chale_Ayenge_Bihari_Sargam_Harmonium__Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =126)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yashomati_Maiya_Se_Bole_Nandlala_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =127)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gaiya_Maiya_Bula_Rahi_Hai_Harmonium_Sargam__Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =128)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kya_Khoob_Lagti_Ho_Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =131)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Tumhe_Chahte_Hain_Aise_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =132)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Hi_Re_Song_Piano_Notations__Keyboard_Western_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =140)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Desh_Ki_Dharti_Notes_for_Piano_and_Harmonium___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =141)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bachpan_Ki_Mohabbat_Ko__Baiju_Bawra__Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =151)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aap_Ki_Nazron_Ne_Smjha_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =153)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ab_To_Hai_Tumse_Song_Sargam__Piano_Notes_in_Hindi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =154)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chalte_Chalte_Yunhi_Koi_Sargam__Harmonium_Notes__Piano_Notation___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =156)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Woh_Jab_Yaad_Aaye_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =162)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saajan_Mera_Us_Paar_Hai_Sargam_Harmonium__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =164)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Do_Teen__Tezaab__Song_Harmonium_Sargam__Piano_Notes_in_Hindi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =165)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Do_Teen__Old_Song__Piano_Notes__CDF_Notations_for_Keyboard___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =166)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dheere_Dheere_Se_Meri_Zindagi_Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =174)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pardesi_Pardesi_Jana_Nahi_Notes__Sargam_in_Hindi_for_Harmonium_and_Piano___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =175)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kitna_Haseen_Chehra__Dilwale__Song_Notes__Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =176)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mera_Dil_Bhi_Kitna_Pagal_Hai_Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =178)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhe_Dekha_To_Ye_Jaana_Sanam_Harmonium_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =179)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Pyar_Ka_Nagma_Hai__Shor__keyboard_Piano_Notations_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =183)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dheere_Dheere_Se_Meri_Zindagi_Mein_Piano_Keyboard_Notes_in_CDF___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =185)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Pyar_Ka_Nagma_Hai_Harmonium_Notes__Sargam__Sa_Re_Ga_Ma_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =186)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mile_Ho_Tum_Humko_Piano_Notes_in_English__CDF_Notations____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =215)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hothon_Se_Chhulo_Tum_Song_Sargam__Piano_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =218)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hai_Apna_Dil_To_Awara_Piano_Notes_in_Hindi__Harmonium_Sargam____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =219)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chupke_Chupke_Raat_Din_Ghulam_Ali_Ghazal_Notes_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =223)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jana_Gana_Mana_National_Anthem_Harmonium_Notes_Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =229)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Krishna_Bhajan_Mohan_Se_Dil_Kyun_Lagaya_Hai_Notes_Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =230)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sare_Jahan_Se_Acha_Hindustan_Humara_Harmonium_Notes__Piano_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =233)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jai_Ganesh_Jai_Ganesh_Jai_Ganesh_Deva_Harmonium_Notes__Sargam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =234)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Om_Jai_Jagdish_Hare_Aarti_Harmonium_Notes__Slow_Tutorial____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =235)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Om_Jai_Jagdish_Hare_Aarti_Harmonium_Piano_Notes_in_Hindi__sargam____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =237)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gayati_Mantra_Piano_Notes_and_Harmonium_Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =239)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Om_Jai_Jagdish_Hare_Aarti_Piano_Notes_and_Tutorial___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =241)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dar_Chhod_Ke_Jaunga_Na_Maiya_Bhajan_Sargam__Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =245)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Hi_Ho__Aashqui_2__Sargam__Hindi_Notes_for_Harmonium_Piano___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =250)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Rashke_Qamar_Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =252)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aa_Jao_Bhole_Baba_Mere_Makan_Mein_Sargam_Harmonium__Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =256)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Honge_Kamyab_Song_Harmonium_Notations__Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =258)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aye_Mere_Watan_Ke_Logo_Piano_Harmonium_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =261)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Vande_Mataram_Song_Notes_for_Piano_and_Harmonium___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =262)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_To_Thehre_Pardesi__Altaf_Raja__Harmonium_Notes__Piano_Notations___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =286)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mann_Dole_Mera_Tann_Dole_Sargam_Notes_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =295)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rang_Barse_Bheege_Chunar_Wali_Harmonium_Notes_Sargam_in_Hindi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =343)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dekhte_Dekhte__Batti_Gul_Meter_Chalu____Sargam_And_Flute_(request):
	text = Sargams.objects.filter(id__iexact =379)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Moh_Moh_ke_dhaage__Dum_Laga_Ke_Haisha____Sargam_And_Flute_(request):
	text = Sargams.objects.filter(id__iexact =380)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baarish_Lete_Aana__Darshan_Raval____Sargam_And_Flute_(request):
	text = Sargams.objects.filter(id__iexact =381)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Intezaar__Arijit_Singh____Sargam_And_Flute_(request):
	text = Sargams.objects.filter(id__iexact =382)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pal_Pal_Dil_Ke_Paas__Kishore_Kumar____Sargam_And_Flute_(request):
	text = Sargams.objects.filter(id__iexact =383)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Rahoon_Ya_Na_Rahoon__Armaan_Malik____Sargam_And_Flute_(request):
	text = Sargams.objects.filter(id__iexact =384)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Mileya__Darshan_Raval____Sargam_And_Flute_(request):
	text = Sargams.objects.filter(id__iexact =385)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bechara_dil_kya_kare___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =498)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Banjara__Jaise_Banjare_Ko_Ghar____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =499)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bhor_bhaye_panghat_pe___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =500)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bavra_Mann_Dekhne_Chala_Ek_Sapna___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =501)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bahut_Pyar_Karte_Hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =502)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bhigi_bhigi_rato_me___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =503)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bheege_hont_tere___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =504)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bheegi_Bheegi_Si_Hai_Raatein___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =505)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bahut_door_mujhe_chale_jana_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =506)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bahon_me_chale_aao___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =507)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baar_baar_din_ye_aye__happy_birthday____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =508)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aye_mere_watan_ke_logo___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =509)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Awarapan__Banjarapan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =510)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Babuji_dheere_chalna___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =511)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bade_Achhe_lagte_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =512)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Awaz_deke_hame_tum_bulao___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =513)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zindagi_mil_ke_bitayenge___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =514)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zara_zara_mehekta_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =515)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zindagi_kaisi_hai_paheli_haye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =516)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_raate_ye_mausam_ye_nadi_ka_kinara___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =517)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_raat_ye_chandni_fir_kahan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =518)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_nayan_dare_dare___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =519)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_moh_moh_ke_dhaage___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =520)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_kya_hua___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =521)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_jo_mohabbat_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =522)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_Jawani_Hai_Diwani___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =523)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_haseen_Wadiya_Ye_Khula_Asmaan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =524)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_dil_ye_paagal_dil_mera___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =525)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_dil_Diwana_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =526)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_Awara_Raatein___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =527)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_Jeevan_Hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =528)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yamma_Yamma___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =529)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yaadon_Ki_Baraat___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =530)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Wo_shaam_kuchh_ajeeb_thi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =531)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Waqt_ne_kiya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =532)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Wada_raha_sanam___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =533)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Vande_Mataram__Anand_Math____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =534)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Wada_karo_nahi_chhorogi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =535)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tune_Mere_Jana__Emptiness____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =536)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def tumse_milke_aisa_laga___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =537)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumhen_yaad_karte_karte___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =538)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumse_Hi__Na_hai_ye_paana_______Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =539)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumse_kahoon_ek_baat_paron_se_halki_halki___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =540)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumane_mujhe_dekha___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =541)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_se_hi_din_hota_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =542)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_pukar_lo___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =543)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumhe_apna_banaane_ki_kasam___ka_junoo___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =544)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Paas_Aaye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =545)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_itna_jo_muskura_rahe_ho___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =546)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_mile_to_jeena_aa_gaya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =547)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Dil_ki_dhadkan_me___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =548)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_bin_jiya_jaye_kaise___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =549)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_bhi_chalo___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =550)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhe_dekh_dekh_sona___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =551)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhse_naraz_nahi_zindagi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =552)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhe_Suraj_Kahu_ya_Chanda___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =553)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_tu_hai_wahi_dil_ne_jise___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =554)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Mile_Dil_Khile___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =555)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Hi_Re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =556)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_meri_meri_teri___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =557)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_mast_mast_do_nain___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =558)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_liye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =559)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_bina_zindagi_se___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =560)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_galliyan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =561)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_bina_jiya_jaye_na___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =562)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_bin_tere_bin___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =563)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_bin_nayi_lagda_dil_mera_dholna___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =564)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tanhayee___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =565)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Surmayee_ankhiyon_me___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =566)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tadap_Tadap_ke_is_dil_se___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =567)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Suno_na_sange_marmar_ki___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =568)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Suno_gaur_sey_duniya_walon___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =569)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sunn_raha_hai_na_tu___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =570)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Solah_baras_ki_bali_umar_ko_salam___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =571)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Shyam_teri_bansi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =572)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Seene_me_jalan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =573)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sawan_ka_mahina___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =574)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Satyam_Shivam_Sundaram___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =575)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sathiya_tune_kya_kiya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =576)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saranga_teri_yaad_me___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =577)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sapne_me_sajan_se_do_batein___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =578)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanwaar_loon___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =579)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanam_Re_sanam_re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =580)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saiyyan__Heere_Moti_main_na_chahu____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =581)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Roop_tera_mastana___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =582)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rimjhim_Gire_Sawan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =583)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rimjhim_Rimjhim_Rumjhum_Rumjhum___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =584)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rasik_Balma___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =585)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ranjish_Hi_Sahi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =586)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rang_Barse_Bhige_Chunar_Wali___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =587)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Raat_Kali_ek_khwaab_mein_aayee___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =588)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pyar_Diwana_Hota_Hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =589)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pukarta_chalaa_hun_mein___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =590)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Puchho_na_kaise_maine_rain_bitai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =591)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Piya_to_se_naina_lage_re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =592)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Piya_Re_Piya_Re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =593)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phoolon_Ka_Taron_Ka___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =594)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehla_nasha_pehla_khumar___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =595)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pardesiya_ye_sach_hai_piya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =596)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pankh_Hote_Toh_Udd_Aati_Re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =597)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pani_da_rang_wekh_ke___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =598)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pal_Pal_Pal___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =599)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pal_pal_dil_ke_paas___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =600)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_Sajnaa__barakha_bahaar_aayee___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =601)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_ri_chiraiya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =602)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_saathi_re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =603)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_Re_Piya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =604)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_re_manva_tu_kyu_bavra_hai__Iktara____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =605)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_majhi_re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =606)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_hansini___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =607)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_mere_dil_ke_chain___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =608)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Neele_Gagan_Ke_Tale___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =609)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Neela_asman_so_gaya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =610)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Nanha_Munna_Rahi_Hu___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =611)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Naino_me_badra_chhaye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =612)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Naina_Barse_Rim_jhim_Rim_jhim___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =613)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Nahi_Nahi_Abhi_Nahi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =614)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Nadiya_se_Dariya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =615)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Na_maaye_naa_bhej_mujhe___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =616)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Muthukodi_Kawadi_Hada___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =617)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Musafir_Hu_Yaro___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =618)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mujhko_is_raat_ki_tanhayi_me___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =619)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def More_saiyyan_to_hai_pardes___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =620)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mohabbaten_Lutaungaa___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =621)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mitwa__Mere_man_ye_bata_de_tu____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =622)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Meri_bhigi_bhigi_si___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =623)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_rashk_e_kamar___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =624)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Rang_Mein_rangne_wali___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =625)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Nishaan__OMG____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =626)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_naina_sawan_bhadon___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =627)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_mehboob_qayamat_hogi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =628)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_khwabo_me_jo_aye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =629)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_hath_mein___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =630)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_dil_me_aj_kya_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =631)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mera_mulk_mera_desh___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =632)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Megha_chhaye_aadhi_raat___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =633)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Manwa_Lage___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =634)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Man_re_tu_kahe_na_dhir_dhare___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =635)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Man_Mast_Magan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =636)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_tenu_samjhawa_ki___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =637)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_rahu_ya_na_rahu___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =638)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mai_ye_soch_kar_uske_dar_se___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =639)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Kabhi_Batlata_Nahin__Maa____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =640)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mai_shayar_badnam___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =641)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Madhosh_dil_ki_dhadkan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =642)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lukka_chuppi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =643)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lambi_Judaai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =644)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Laila_main_laila___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =645)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lag_Ja_Gale___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =646)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kyuki_Tum_Hi_Ho___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =647)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kyu_na_bole_mose_mohan_kyu___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =648)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kya_yehi_pyar_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =649)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kurbaan_Hua___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =650)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kuhu_Kuhu_bole_koyaliya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =651)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kora_Kagaz_Tha_Yeh_Mann_Mera___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =652)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Koi_ye_kaise_bataaye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =653)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Koi_Humdum_Na_Raha___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =654)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kiska_rasta_dekhe___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =655)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Khoya_Khoya_Chand_Khula_Aasman___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =656)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kehna_hai__Kehna_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =657)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaun_hai_jo_sapno_me_aya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =658)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kasme_vade_pyar_wafa_sab___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =659)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kash_tere_ishq_me_nilam_ho_jau___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =660)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kariye_Na_Kariye_Na___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =661)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kal_ho_na_ho__Har_ghadi_badal_rahi_hai_______Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =662)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kahin_Karti_Hogi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =663)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kahin_door_jab_din_dhal_jaye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =664)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaha_tak_ye_man_ko___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =665)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabhi_Sham_Dhale___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =666)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabhi_kabhi_mere_dil_me___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =667)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ka_Karu_Sajni_Aye_na_baalam___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =668)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jogi_Jab_Se_Yu_Aya_Mere_Dware___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =669)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jeene_Laga_Hoon___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =670)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jeena_Yahan_Merna_Yahan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =671)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jeena_Jeena___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =672)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jaun_kahan_bata_aye_dil___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =673)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jashn_e_bahara___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =674)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Janeman_Janeman_Tere_Do_Nayan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =675)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jane_Woh_Kaise_Log_The___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =676)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jane_kyu_log_mohabbat_kiya_karte_ha___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =677)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jane_kya_dhoondti_rehti_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =678)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jane_Kahan_Gaye_Wo_Din___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =679)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jane_do_na__Paas_aao_na___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =680)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Janam_janam_janam___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =681)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jai_jai_shiv_shankar___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =682)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jab_koi_baat_bigad_jaaye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =683)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jaane_Kya_Baat_Hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =684)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Itna_na_mujhase_tu_pyar_badha___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =685)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jaane_ja_dhundhta_fir_raha___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =686)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Itni_shakti_hame_dena_daata___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =687)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Isharo_isharo_me_dil_lene_wale___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =688)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ik_hasee_shaam_ko___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =689)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ik_aisi_ladki_thi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =690)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_tere_sheher_me_aye_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =691)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humma_humma__ik_ho_gaye_hum_aur_tum____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =692)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_tere_bin_ab_jee_nahi_sakte__Kyuki_Tum_hi_ho____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =693)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_dono_do_premi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =694)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_rahe_ya_na_rahe_kal___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =695)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_dil_de_chuke_sanam___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =696)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Bewafa_Hargeez_Na_The___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =697)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Aapke_Hain_Kaun___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =698)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hoshwalo_ko_khabar_kya___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =699)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hothon_se_chhoo_lo_tum___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =700)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Har_kisi_ko_nahi_milta__Do_Lafz_ki_hai____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =701)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hame_tumse_pyaar_kitna___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =702)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hamari_Adhuri_Kahani__Title_Song____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =703)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hai_apna_dil_to_awara___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =704)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gumnam_hai_koi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =705)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gulabi_ankhen_jo_teri_dekhi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =706)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ghungroo_ki_tarah___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =707)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ghar_jayegi_tar_jayegi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =708)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ghar_Aaya_Mera_Pardesi___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =709)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gerua__Dhoop_se_nikal_ke____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =710)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Ladki_ko_dekha_to___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =711)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_daal_par_tota_bole___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =712)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ehsaan_Tera_Hoga_Mujh_Par___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =713)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Ajnabi_Haseena_Se___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =714)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Doraemon_theme_song__Hindi____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =715)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Doston_se_jhooti_mooti___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =716)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Doli_me_bithai_ke_kahar___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =717)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Do_Lafzon_Ki_Hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =718)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_to_bachcha_hai_ji___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =719)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Din_dhal_jaye___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =720)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Se_Re______Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =721)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Smbhal_ja_zara___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =722)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Pukare_Aare_Aare_Aare___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =723)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_ne_kaha_chupke_se___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =724)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_lootne_wale_jadugar___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =725)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Hoom_Hoom_Kare___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =726)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_diydiyan_gallan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =727)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_hai_chota_sa___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =728)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_diya_hai_jaan_bhi_denge___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =729)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dhadkan_zara_ruk_gayi_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =730)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dekha_Na_Haay_Re___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =731)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Deewana_hua_baadal___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =732)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dard_dilo_ke_kam_ho_jate___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =733)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chura_liya_hai_tumne_jo___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =734)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chupke_Chupke_Raat_Din___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =735)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chup_chup_khade_ho___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =736)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chori_chori_teri_meri_love_story___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =737)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Choodi_nahi_ye_mera___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =738)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chingari_koyi_bhadake___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =739)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chhupa_Lo_yun_Dil_me___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =740)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chhoo_kar_mere_man_ko___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =741)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chehra_hai_ya_chand_khila___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =742)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chak_Dhoom_Dhoom_____Koi_Ladki_Hai_Jab_Wo_Hasti_Hai____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =743)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chandan_sa_badan___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =744)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chaha_tujhe_hai__Band_of_Boys____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =745)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chaha_Hai_Tujhko___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =746)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Breathless___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =747)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bolna_Mahi_Bolna___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =748)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Apki_ankhon_me_kuchh___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =749)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ankhon_me_teri_ajab_si___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =750)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Albela_sajan_aayo_ree___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =751)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Alvida__alvida___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =752)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Akele_hai_to_kya_gham_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =753)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aja_re_mai_to_kab_se___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =754)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aj_jane_ki_zid_na_karo___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =755)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aise_na_mujhe_tum_dekho___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =756)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ahatein_ho_rahi_teri__MTV_Splitsvilla____Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =757)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ae_Zindagi_Gale_Laga_Le___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =758)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Abhi_naa_jao_chhod_kar___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =759)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Abhi_mujh_mein_kahin___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =760)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aawara_hoon___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =761)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ab_To_Hai_Tumse___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =762)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aate_jate_hanste_gaate___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =763)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aap_ke_haseen_rukh_pe___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =764)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaoge_jab_tum_o_saajna___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =765)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aao_na_gale_lagalo_na___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =766)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaja_sanam_madhur_chandni_mein_hum___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =767)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aane_wala_pal_jane_wala_hai___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =768)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aa_jaane_ja___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =769)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaja_aaja_mai_hu_pyaar_tera___Notes___Sargam(request):
	text = Sargams.objects.filter(id__iexact =770)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumhe_Apna_Banane_Ka_Guitar_Tabs___Lead___Hate_Story_3___AbhijeetChaar_Kadam_Guitar_Tabs___Lead___PK_2014____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =1)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Phir_Tumpe_Pyar_Aaya_Hai_Guitar_Tabs___Lead___Hate_Story_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =2)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Chahiye_Guitar_Tabs___Lead___Bajrangi_Bhaijaan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =3)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kya_Mujhe_Pyar_Hai_Guitar_Tabs___Lead___Woh_Lamhe___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =4)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def BAARISH_Guitar_Tabs___Lead___Yaariyan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =5)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Aaj_Kal_Guitar_Tabs___Lead___Purani_Jeans___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =6)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def HUMDARD_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =7)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Mar_Jayenge__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =8)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saanson_Ko_Jeene_Ka_Guitar_Tabs___Lead___Zid__2014____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =9)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Share_a_link_on_Twitter(request):
	text = Sargams.objects.filter(id__iexact =10)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Meri_Teri_Meri_Guitar_Tabs___Lead___Bodygaurd___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =11)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lag_Ja_Gale_Guitar_Tabs___Lead___Woh_Kaun_Thi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =12)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Muskurane_Ki_Wajah_Tum_Ho_Guitar_Tabs___Lead___City_Lights___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =13)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bin_Tere__Reprise__Guitar_Tabs___Lead___I_Hate_Love_Stories___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =14)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Iktara_Guitar_Tabs___Lead___Wake_Up_Sid___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =15)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Luka_Chuppi_Bahut_Huyi_Guitar_Tabs___Lead___Rang_De_Basanti___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =16)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Muskurane_Ki_Wajah_Tum_Ho_Guitar_Tabs___Lead___City_Lights___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =17)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Iktara_Guitar_Tabs___Lead___Wake_Up_Sid___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =18)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Dil_Shayrana_Guitar_Tabs___Lead___Holiday___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =19)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Galliyan_Teri_Galiyan_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =20)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Rang_Sharbaton_Ka__Phata_Poster_Nikla_Hero__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =21)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humnava_Guitar_Tabs___Lead___Humari_Adhuri_Kahani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =22)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rehnuma_Guitar_Tabs___Lead___ROCKY_HANDSOME___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =23)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Naam_Hamne_kiya_hai_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =24)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sun_Raha_Hai_na_tu__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =25)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaise_Mujhe_Tum_Mil_Gayi_Guitar_Tabs___Lead___Ghajini___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =26)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Mehboob_Qayamat_Hogi_Guitar_Tabs___Lead___Mr_X_In_Bombay___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =27)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aashiyan_Guitar_tabs__Barfi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =28)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Hi_Tu_Har_Jagah_Guitar_Tabs___Lead___KICK__2014____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =29)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Ladki_Ko_Dekha_To_Aisa_Laga_Guitar_Tabs___Lead___1942_Love_Story___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =30)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Hone_Laga_Hoon_Guitar_Tabs___Lead___Ajab_Prem_Ki_Ghazab_Kahani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =31)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humko_Humise_Chura_Lo_Guitar_Tabs___Lead___Mohabbatein_Tune___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =32)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Neele_Neele_Ambar_Par_Guitar_Tabs___Lead___Kalakaar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =33)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dheere_Dheere_Se_Guitar_Tabs___Lead___Aashiqui__1990____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =34)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def PANI_DA_RANG_vekh_ke_Guitar_Tabs___Lead___Vicky_Donor___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =35)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Re_Kabira_maan_jaa_Guitar_Tabs___Lead__Yeh_Jawaani_Hai_Deewani____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =36)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Paas_Aaye_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =37)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Agar_Tum_Saath_Ho_Guitar_Tabs___Lead___Tamasha___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =38)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehla_Nasha_Pehla_Hummar_Guitar_Tabs___Lead___Jo_Jeeta_Wohi_Sikandar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =39)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Chehra_Guitar_Tabs___Lead___SANAM_TERI_KASAM___ARIJIT_SINGH___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =40)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chura_Liya_Hai_Tumne_Jo_Dil_Ko_Guitar_Tabs___Lead___Yaadon_Ki_Baarat___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =41)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baatein_Ye_Kabhi_Na_Guitar_Tabs___Lead___Khamoshiyan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =42)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kal_Ho_Naa_Ho_Guitar_Tabs___Lead___Title_Track___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =43)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_Pehli_Baar_Mohabbat_Ki_Hai_Guitar_Tabs___Lead___Sirf_Tum___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =44)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_O_Jaane_Jaana_Guitar_Tabs___Lead___Pyar_Kiya_To_Darna_Kya___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =45)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Haseena_Thi_Ek_Deewana_Tha_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =46)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gulabi_Aankhein_Jo_Teri_Dekhi_Guitar_Tabs___Lead___The_Train___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =47)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hua_Hai_Aaj_Pehli_Baar_Guitar_Tabs___Lead___Sanam_Re___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =48)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Raabta_Guitar_Tabs___Lead___Agent_Vinod___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =49)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bolna_Guitar_Tabs___Lead____Kapoor_and_Sons__Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =50)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gerua_Guitar_Tabs___lead___Dilwale__2015____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =51)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Rahoon_Ya_Na_Rahoon_Guitar_Tabs___Lead___Armaan_Malik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =52)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Hoon_Hero_Tera_Guitar_Tabs___Lead___Hero__Salman_Khan____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =53)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chahun_Main_Ya_Na__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =54)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def JEENA_JEENA_Guitar_Tabs___Lead___Badlapur__Atif_Aslam____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =55)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhe_Dekha_To_Ye_Jaana_Sanam_Guitar_Tabs___Lead___DDLJ_Tune___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =56)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabhi_Jo_Baadal_Barse_Guitar_Tabs___Lead__Jackpot____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =57)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Tenu_Samjhawan_Ki_Guitar_Tabs___Lead___Humpty_Sharma_Ki_Dulhania___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =58)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanam_Re_Guitar_Tabs___Lead___Sanam_Re__Arijit_Singh____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =59)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ishq_Wala_Love_Guitar_Tabs___Lead___Student_of_the_Year__SOTY____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =60)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_hi_ho__Ashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =61)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Soch_Na_Sake_Guitar_Tabs___Lead___Airlift__Arijit_Singh____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =62)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Janam_Janam_Guitar_Tabs___Lead___Dilwale__2015____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =63)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def List_of_Best_Bollywood_Guitar_Songs_of_all_the_time___Best_Hindi_Songs__2015____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =64)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Hoon_Hero_Tera_Guitar_Tabs___Lead___Hero__Salman_Khan____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =65)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Rahoon_Ya_Na_Rahoon_Guitar_Tabs___Lead___Armaan_Malik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =66)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumhe_Apna_Banane_Ka_Guitar_Tabs___Lead___Hate_Story_3___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =67)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Agar_Tum_Saath_Ho_Guitar_Tabs___Lead___Tamasha___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =68)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gerua_Guitar_Tabs___lead___Dilwale__2015____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =69)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Janam_Janam_Guitar_Tabs___Lead___Dilwale__2015____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =70)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanam_Re_Guitar_Tabs___Lead___Sanam_Re__Arijit_Singh____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =71)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Soch_Na_Sake_Guitar_Tabs___Lead___Airlift__Arijit_Singh____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =72)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hua_Hai_Aaj_Pehli_Baar_Guitar_Tabs___Lead___Sanam_Re___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =73)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabhi_Jo_Baadal_Barse_Guitar_Tabs___Lead__Jackpot____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =74)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Meri_Maa_Mumma_Guitar_Tabs___Lead___Kailash_Kher__Dasvidaniya____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =75)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saathiya_Pagle_Se_Dil_Ne_Ye_Kya_Kiya_Guitar_Tabs___Lead___Singham___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =76)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chhoti_Si_Pyari_Si_Nanhi_Si_Guitar_Tabs___Lead___Anari___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =77)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aashiyan_Guitar_tabs__Barfi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =78)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phoolon_Sa_Chehra_Tera_Guitar_Tabs___Lead___Anari___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =79)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_hi_ho__Ashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =80)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Rang_Sharbaton_Ka__Phata_Poster_Nikla_Hero__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =81)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sun_Raha_Hai_na_tu__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =82)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chahun_Main_Ya_Na__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =83)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aashiqui_2_love_theme_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =84)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Mar_Jayenge__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =85)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh_Guitar_Tabs___Lead___Best_of_Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =86)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ashiqui_2_Movie_Guitar_Tabs___Lead___All_Songs_of_Ashiqui_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =87)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Re_Kabira_maan_jaa_Guitar_Tabs___Lead__Yeh_Jawaani_Hai_Deewani____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =88)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhe_Dekha_To_Ye_Jaana_Sanam_Guitar_Tabs___Lead___DDLJ_Tune___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =89)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_O_Jaane_Jaana_Guitar_Tabs___Lead___Pyar_Kiya_To_Darna_Kya___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =90)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gulabi_Aankhein_Jo_Teri_Dekhi_Guitar_Tabs___Lead___The_Train___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =91)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Iktara_Guitar_Tabs___Lead___Wake_Up_Sid___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =92)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Paas_Aaye_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =93)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Naam_Hamne_kiya_hai_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =94)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def BAARISH_Guitar_Tabs___Lead___Yaariyan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =95)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Haseena_Thi_Ek_Deewana_Tha_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =96)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def PANI_DA_RANG_vekh_ke_Guitar_Tabs___Lead___Vicky_Donor___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =97)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehla_Nasha_Pehla_Hummar_Guitar_Tabs___Lead___Jo_Jeeta_Wohi_Sikandar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =98)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Naina_Maar_Hi_Daalenge_Guitar_tabs___Jai_Ho___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =99)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Aaj_Kal_Guitar_Tabs___Lead___Purani_Jeans___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =100)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kyon_na_hum_tum_Guitar_Tabs__Barfi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =101)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Mehboob_Qayamat_Hogi_Guitar_Tabs___Lead___Mr_X_In_Bombay___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =102)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Raabta_Guitar_Tabs___Lead___Agent_Vinod___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =103)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Galliyan_Teri_Galiyan_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =104)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def TU_HI_HAI_AASHIQUI_Guitar_Tabs___Dishkiyaoon___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =105)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Khali_Salam_Dua_Guitar_Tabs___Shortcut_Romeo___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =106)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Muskurane_Ki_Wajah_Tum_Ho_Guitar_Tabs___Lead___City_Lights___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =107)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Suno_Na_Sangemarmar_Guitar_Tabs___Youngistaan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =108)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humko_Humise_Chura_Lo_Guitar_Tabs___Lead___Mohabbatein_Tune___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =109)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kal_Ho_Naa_Ho_Guitar_Tabs___Lead___Title_Track___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =110)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Phir_Tumpe_Pyar_Aaya_Hai_Guitar_Tabs___Lead___Hate_Story_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =111)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Tenu_Samjhawan_Ki_Guitar_Tabs___Lead___Humpty_Sharma_Ki_Dulhania___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =112)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Dil_Shayrana_Guitar_Tabs___Lead___Holiday___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =113)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Meri_Teri_Meri_Guitar_Tabs___Lead___Bodygaurd___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =114)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chura_Liya_Hai_Tumne_Jo_Dil_Ko_Guitar_Tabs___Lead___Yaadon_Ki_Baarat___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =115)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Luka_Chuppi_Bahut_Huyi_Guitar_Tabs___Lead___Rang_De_Basanti___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =116)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Papa_Kehte_Hain_Bada_Naam_Karega_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =117)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Dil_Ki_Dhadkan_Mein_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =118)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dard_Dilo_Ke_Guitar_Tabs___Lead___The_Xpose___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =119)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Banjara_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =120)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def HUMDARD_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =121)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ishq_Wala_Love_Guitar_Tabs___Lead___Student_of_the_Year__SOTY____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =122)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Hi_Tu_Har_Jagah_Guitar_Tabs___Lead___KICK__2014____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =123)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sandese_Aate_Hain_Guitar_Tabs___Lead___Border___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =124)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Happy_Birthday_To_You_Guitar_Tabs___Lead___Bday_Song_Tune___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =125)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Raghupati_Raghav_Raja_Ram_Guitar_Tabs___Lead___Ram_Bhajan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =126)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Hone_Laga_Hoon_Guitar_Tabs___Lead___Ajab_Prem_Ki_Ghazab_Kahani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =127)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaise_Mujhe_Tum_Mil_Gayi_Guitar_Tabs___Lead___Ghajini___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =128)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hai_Dil_Ye_Mera_Guitar_Tabs___Lead___Hate_Story_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =129)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jumme_Ki_Raat_Hai_Guitar_Tabs___Lead___Kick__2014____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =130)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Naam_Doon_Guitar_Tabs___Lead___Its_Entertainment___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =131)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabhi_Aayine_Pe_Guitar_Tabs___Lead__Aye_Khuda____Hate_Story_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =132)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sawan_Aaya_Hai_Guitar_Tabs___Lead___Creature_3D___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =133)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sukoon_Mila_Guitar_Tabs___Lead___Mary_Kom___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =134)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gulaabi_Aankhen_Jo_Teri_Dekhi_Guitar_Chords___The_Train__1970____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =135)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Papa_kehte_hain_bada_naam_karega_Guitar_Chords___Qayamat_Se_Qayamat_Tak___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =136)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mera_Mann_Kehne_Laga_Guitar_Tabs___Lead___Nautanki_Saala___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =137)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Khushnuma_Guitar_Tabs___Lead___Suyyash_Rai___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =138)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saanson_Ko_Jeene_Ka_Guitar_Tabs___Lead___Zid__2014____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =139)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chaar_Kadam_Guitar_Tabs___Lead___PK_2014____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =140)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Are_Re_Are_Ye_Kya_Hua_Guitar_Tabs___Lead___Dil_To_Pagal_Hai___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =141)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Raja_Ko_Rani_Se_Pyaar_Ho_Gaya_Guitar_Tabs___Lead___Akele_Hum_Akele_Tum___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =142)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lag_Ja_Gale_Guitar_Tabs___Lead___Woh_Kaun_Thi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =143)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Wo_Lamhe_Wo_baatein_Guitar_Tabs___Lead___Atif_Aslam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =144)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bin_Tere__Reprise__Guitar_Tabs___Lead___I_Hate_Love_Stories___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =145)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bikhra_Hoon_Main_Guitar_Tabs___Lead___Aadat__Jal_The_Band____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =146)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baatein_Ye_Kabhi_Na_Guitar_Tabs___Lead___Khamoshiyan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =147)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kya_Mujhe_Pyar_Hai_Guitar_Tabs___Lead___Woh_Lamhe___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =148)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def JEENA_JEENA_Guitar_Tabs___Lead___Badlapur__Atif_Aslam____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =149)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_Pehli_Baar_Mohabbat_Ki_Hai_Guitar_Tabs___Lead___Sirf_Tum___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =150)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mitti_di_khushboo_Guitar_Tabs___Lead___Ayushmann_Khurrana___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =151)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dheere_Dheere_Se_Guitar_Tabs___Lead___Aashiqui__1990____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =152)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Ladki_Ko_Dekha_To_Aisa_Laga_Guitar_Tabs___Lead___1942_Love_Story___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =153)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Doorie_Sahi_Jaye_Na_Guitar_Tabs___Lead___Atif_Aslam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =154)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Laila_Tu_Saamne_Kyun_Na_Aaye_Guitar_Tabs___Lead___Faridkot___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =155)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sooraj_Dooba_Hai_Yaaron_Guitar_Tabs___Lead___Roy___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =156)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Chahiye_Guitar_Tabs___Lead___Bajrangi_Bhaijaan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =157)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sawan_Ka_Mahina_Pawan_Kare_Guitar_Tabs___Lead___Milan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =158)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yaaron_Dosti_Badi_Hi_Haseen_Hai_Guitar_Tabs___Lead___k_k___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =159)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humnava_Guitar_Tabs___Lead___Humari_Adhuri_Kahani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =160)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Leke_Pehla_Pehla_Pyaar_Guitar_Tabs___Lead___CID__1956____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =161)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Saamne_Wali_Khidki_Mein_Guitar_Tabs___Lead___Padosan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =162)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Agar_Tum_Mil_Jao_Guitar_Tabs___Lead___Zeher___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =163)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sajda_Guitar_Tabs___Lead___My_Name_Is_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =164)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Neele_Neele_Ambar_Par_Guitar_Tabs___Lead___Kalakaar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =165)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Naina_Tere_Naina_Guitar_Tabs___Lead___My_Name_Is_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =166)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Chehra_Guitar_Tabs___Lead___SANAM_TERI_KASAM___ARIJIT_SINGH___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =167)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Meri_Kahaani_Guitar_Tabs___Lead___Gabbar_is_Back___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =168)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chunar_Guitar_Tabs___Lead___ABCD_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =169)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bolna_Guitar_Tabs___Lead____Kapoor_and_Sons__Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =170)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sun_Saathiya_Guitar_Tabs___Lead___ABCD_2__Any_Body_Can_Dance_2____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =171)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rehnuma_Guitar_Tabs___Lead___ROCKY_HANDSOME___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =172)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humari_Adhuri_Kahani_Guitar_Tabs___Lead___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =173)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baaton_Ko_Teri_Guitar_Tabs___Lead___All_is_Well___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =174)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Bin_Nahi_Laage_Guitar_Tabs___Lead___Ek_Paheli_Leela___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =175)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Panchhi_Nadiya_Pawan_Ke_Jhonke_Guitar_Tabs___Lead___Refugee___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =176)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Deewani_Mastani_Guitar_Tabs___Lead___Bajirao_Mastani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =177)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def List_of_Best_Bollywood_Hindi_Love_Songs___Valentine_Day_Songs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =178)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Shreya_Ghoshal_Guitar_Tabs___Lead___Best_of_Shreya_Ghoshal___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =179)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Wafa_Ne_Bewafai_Guitar_tabs___Lead___Teraa_Suroor___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =180)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sab_Tera_Guitar_Tabs___Lead___BAAGHI___ARMAAN_MALIK__SHRADDHA_KAPOOR___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =181)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Woh_Chaand_Guitar_Tabs___Lead___TERAA_SURROOR___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =182)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ijazat_Guitar_Tabs___Lead___ONE_NIGHT_STAND___ARIJIT_SINGH___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =183)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bol_Do_Na_Zara_Guitar_Tabs___Lead___Azhar___Armaan_Malik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =184)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bekhudi_Guitar_Tabs___Lead___Teraa_Surroor___Darshan_Raval___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =185)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yeh_Fitoor_Mera_Guitar_Tabs___Lead___Fitoor___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =186)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Manwa_Behrupiya_Guitar_Tabs___Lead___Bollywood_Diaries___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =187)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atrangi_Yaari_Guitar_Tabs___Lead___Wazir___Farhan_Akhtar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =188)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Bin_Guitar_Tabs___Lead___Wazir___Sonu_Nigam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =189)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanam_Teri_Kasam_Guitar_Tabs___Lead___Ankit_Tiwari___Mohammed_Irfan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =190)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Te_Amo_Guitar_Tabs___Lead___Dum_Maro_Dum___Ash_King___Sunidhi_Chauhan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =191)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phir_Mohabbat_Karne_Chala_Guitar_Tabs___Lead___Murder_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =192)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhse_Naraaz_Nahin_Zindagi_Guitar_Tabs___Lead___Masoom___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =193)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ambarsariya_Guitar_Tabs___Lead___Fukrey___Sona_Mohapatra___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =194)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jabra_Fan_Guitar_Tabs___Lead___Fan___Nakash_Aziz___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =195)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Itni_Si_Baat_Hai_Guitar_Tabs___Lead___Azhar___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =196)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Salamat_Guitar_Tabs___Lead___SARBJIT___ARIJIT_SINGH__TULSI_KUMAR___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =197)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Maninder_Buttar___Laare_Chords_with_Strumming_Pattern___Guitar___B_Praak___Jaani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =198)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy_Capo___Vishal_Mishra___Teri_Hogaiyaan_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =199)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Unna_Nenachu_Chords_with_Strumming_Pattern___Psycho___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =200)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Armaan_Malik___Shaamein_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =201)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy_Baari_Chords_with_Strumming_Pattern___Bilaal___Momina_Mustehsan___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =202)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Yeh_Fitoor_Mera_Chords_with_Strumming_Pattern___Guitar____w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =203)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Mera_Mehboob_Chords___Stebin___Guitar___Awez_Darbar___Nagma_Mirajkar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =204)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Accurate___Ullaallaa_Chords_with_Strumming_Pattern___Guitar___Petta___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =205)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jubin_Nautiyal___Main_Janta_Hoon_Chords_with_Strumming_Pattern___Easy___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =206)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Allah_Ve_Chords_with_Strumming_Pattern___Jassie_Gill___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =207)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy__Khuda_Hafiz_Chords_with_Strumming_Pattern___Guitar___The_Body___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =208)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Hi_Yaar_Mera_Chords_with_Strumming_Pattern___Pati_Patni_Aur_Woh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =209)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bypass_Road___Easy___Tanha_Mera_Pyaar_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =210)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Good_Newwz__Maana_Dil_Chords_with_Strumming_Pattern___Guitar___B_Praak___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =211)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh__Easy_Raanjhana_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =212)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jubin_Nautiyal__Tujhe_Kitna_Chahein_Aur_Hum_Chords___Kabir_Singh__Film_Version____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =213)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ja_Chali_Ja_Guitar_Chords_with_Strumming_Pattern___Rishabh_Tiwari___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =214)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabir_Singh___Guitar__Kaise_Hua_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =215)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehla_Pyaar_Chords_with_Strumming_Pattern__Guitar____Kabir_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =216)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Article_15__Intezari_Chords_with_Strumming_Pattern___Armaan_Malik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =217)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Sajna_Ve_Chords_Lisa_Mishra___Vishal_Mishra_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =218)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tere_Bin_Kive_Chords_with_Strumming___Ramji_Gulati___Jannat_Zubair___Mr__Faisu___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =219)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Super_30___Jugraafiya_Chords_with_Strumming_Pattern__Guitar____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =220)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Article_15__Naina_Yeh_Chords_with_Strumming_Pattern__Guitar____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =221)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Tera_Ban_Jaunga_Chords_with_Strumming___Kabir_Singh__w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =222)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Malaal__Zara_Suno_Chords_with_Strumming_Pattern__Guitar____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =223)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Papon___Har_Lamhaa_Chords_with_Strumming_Pattern__Guitar____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =224)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chehre_Padhna_Jaane_Naina___Matvaare_Chords_with_Strumming___Jubin___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =225)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Shawn_Mendes__Señorita_Guitar_Chords_with_Strumming_ft__Camila_Cabello___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =226)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Darshan_Raval___Tu_Mileya_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =227)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Diyan_Gallan_Guitar_Chords_with_Strumming___Tiger_Zinda_Hai___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =228)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy__Chukar_Mere_Man_Ko_Guitar_Chords_with_Strumming___Yaarana___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =229)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kidnap__Monta_Katha_Sonena_Guitar_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =230)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy__Tujhe_Bhula_Diya_Guitar_Chords_with_Strumming__w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =231)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mitti_Di_Khushboo_Guitar_Chords_with_Strum__w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =232)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Guitar__Nanhi_Pari_Chords_by_Sonu_Nigam__Asifa____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =233)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ankit_Tiwari_Guitar__Yeh_Tere_Do_Naina_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =234)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabir_Singh__Tujhe_Kitna_Chahne_Lage_Chords_with_Strumming__w_wo_Guitar_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =235)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy__Tum_Ho_Guitar_Chords_with_Strumming__w_wo_Capo____Rockstar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =236)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def _Easy__Kabir_Singh__Mere_Sohneya_Guitar_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =237)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kidnap___Guitar__Ektu_Jayga_Dena_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =238)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh__Bandeya_Guitar_Chords_with_Strumming___Dil_Junglee___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =239)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def _Easy__Bajrangi_Bhaijaan__Tu_Jo_Mila_Guitar_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =240)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humne_Rait_Pe_Chords_with_Strum___Guitar___Neha_Kakkar___Tony_Kakkar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =241)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zindagi_Di_Paudi_Guitar_Chords_with_Strumming___Millind_Gaba___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =242)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Royee_Jande_Naina_Guitar_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =243)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabira_Guitar_Chords_from_Yeh_Jawaani_Hai_Deewani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =244)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Maa_Guitar_Chords_by_Amitabh_Bachchan___Yajat___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =245)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Student_of_the_Year_2__Fakira_Guitar_Chords_with_Capo_by_Sanam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =246)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def RAETH__Bhula_Do_Bhula_Do_Guitar_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =247)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yaariyaan___Meri_Maa_Guitar_Chords_with_Strum__Two_Versions_Easy____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =248)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ami_Tomake_Bhalobashi_Guitar_Chords___KIDNAP___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =249)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chal_Para_Chords_by_Strings_Band__Guitar_Piano_Ukulele____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =250)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabir_Singh_Guitar__Bekhayali_Chords_with_Strumming__Updated____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =251)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Anxiety_Chords_by_Selena_Gomez___Julia_Michaels___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =252)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ankit_Tiwari___Guitar__Ishq_Kare_Barbadiyaan_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =253)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Indias_Most_Wanted___Guitar__Akela_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =254)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Royi_Jaye_Chords_with_Strumming___Guitar___De_De_Pyar_De___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =255)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaradhana_Ho_Aaradhana_Guitar_Chords___Worship___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =256)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Papon___Guitar__Ik_Mod_Chords_with_Strumming_Pattern___Music_Teacher___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =257)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Bhi_Nahin_Soya_Guitar_Chords___SOTY_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =258)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Music_Teacher__Sambhaal_Rakhiyaan_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =259)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Aas_Paas_Chords___Guitar_by_Yasser_Desai___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =260)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Mila_to_Haina_Chords_with_Capo___Strumming___Guitar___De_De_Pyar_De___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =261)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Se_Teri_Guitar_Chords_with_Strumming___PADMAN___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =262)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Linkin_Park_Numb_Guitar_Chords_with_Capo___Strumming__Easy____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =263)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Somebody_s_Guitar_Chords_with_Capo___Strumming___Enrique_Iglesias___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =264)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def EASY___Teri_Khaamiyan_Guitar_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =265)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def EASY__Tum_Hi_Ho_Guitar_Chords_with_Capo__Strumming___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =266)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhko_Jo_Paaya_Mere_Bina_Guitar_Chords_with_Strumming___Capo___CROOK___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =267)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Muskurane_Ki_Wajah_Guitar_Chords_with_Strumming__Easy____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =268)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def EASY__Mere_Mehboob_Qayamat_Hogi_Guitar_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =269)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mon_Aamar_Chords_by_Arko___Shesh_Theke_Shuru___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =270)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ishqe_Di_Chashni_Guitar_Chords___Strum___Bharat___Salman_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =271)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Chale_Aana_Chords_with_Capo_by_Armaan_Malik___Dede_Pyar_De___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =272)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dhvani_Bhanushali___Guitar__Vaaste_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =273)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tu_Thodi_Der_Chords_with_Capo___Strumming___Half_Girlfriend___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =274)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Music_Teacher___Guitar__Phir_Wahi_Raat_Hai_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =275)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitra__Roke_Na_Ruke_Naina_Chords_with_Capo__Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =276)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Maa_Chords_by_Ankit_Tiwari___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =277)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def KALANK___Guitar__Tabaah_Ho_Gaye_Guitar_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =278)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yasser_Desari___Guitar__Meri_Hasi_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =279)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pora_Mon_Chords_with_Strumming__Easy____Ke_Tumi_Nandini___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =280)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Title_Track___Guitar__Shudhu_Tomari_Jonno_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =281)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aur_Kuch_Baki_Chords_by_Yasser_Desai___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =282)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Eka_Ekela_Mon_Guitar_Chords___Chirodini_Tumi_Je_Amar_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =283)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dosti_Guitar_Chords_with_Strumming_from_Junglee___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =284)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bastushaap___Tomake_Chuye_Dilam_Guitar_Chords___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =285)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def A_Star_Is_Born___SHALLOW_Guitar_Chords_by_Lady_Gaga___Bradley_Cooper___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =286)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Amake_Amar_Moto_Thakte_Dao_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =287)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Shaan___Guitar__Tu_Mera_Rab_Hai_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =288)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sweater___Guitar__Preme_Pora_Baron_Chords__Strumming____Bengali___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =289)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def MS_Dhoni___Guitar__Kaun_Tujhe_Chords__Easy____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =290)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def OK_Jaanu___Guitar__Enna_Sona_Chords_by_Arijit_Singh__Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =291)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def CYPHER___Guitar__Meri_Maa_Chords_by_Sonu_Nigam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =292)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def RAW___Guitar__Bulleya_Chords_by_Rabbi_Shergill___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =293)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def RAW___Guitar__Jee_Len_De_Chords_by_Mohit_Chauhan__Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =294)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def QARAN___Guitar__Haaye_Oye_Chords_ft__Ash_King__Strum____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =295)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Chala_Jata_Hoon_Guitar_Chords_by_Sanam_Puri___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =296)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh___Guitar__Kalank_Guitar_Chords_with_Strumming___Title_Track___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =297)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Junglee___Guitar__Fakeera_Ghar_Aaja_Chords___Jubin_Nautiyal___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =298)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def GUITAR__Sun_Mere_Humsafar_Chords_with_Strumming___Badrinath_Ki_Dulhania___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =299)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Half_Girlfriend___Guitar__Main_Phir_Bhi_Tumko_Chahunga_Chords__w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =300)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jubin_Nautiyal___Guitar__Chitthi_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =301)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Duniyaa_Chords_with_Strumming_Pattern___Luka_Chuppi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =302)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mere_Pyare_Prime_Minister_Chords___Title_Track___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =303)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def KK___Guitar__Tum_Na_Aaye_Chords___Badla___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =304)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def BB_Ki_Vines___Guitar__Bas_Mein_Chords___Bhuvan_Bam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =305)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh___Guitar__Ruan_Ruan_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =306)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mohit_Chauhan___Guitar__Safar_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =307)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notebook___Guitar__Laila_Chords___Dhavani_Bhanushali___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =308)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Total_Dhamaal___Guitar__Mungda_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =309)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darshan_Raval___Guitar__Kaash_Aisa_Hota_Chords__w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =310)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arko___Guitar__Shukriya_Chords___Shokhsanam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =311)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kalank___Guitar__Ghar_More_Pardesiya_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =312)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kesari__Ve_Maahi_Guitar_Chords_with_Strumming_Pattern___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =313)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kesari_Guitar__Teri_Mitti_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =314)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notebook___Guitar__Main_Taare_Chords_by_Salman_Khan__Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =315)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Luka_Chuppi___Guitar__Photo_Chords_with_Capo___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =316)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mujhse_Kaha_Naa_Gaya_Chords___Palash_Sen___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =317)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Teri_Yaad_Chords___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =318)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arko___Guitar__Shukriya_Chords_with_Capo___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =319)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Neha_Kakkar__Tera_Ghata_Chords___Guitar_Version___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =320)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tujhe_Kaise_Pata_Na_Chala_Chords__Reprise____Asees_Kaur___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =321)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tu_Meri_Zindagi_Chords_by_Keshav_Kumar___Rohan_Mehra___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =322)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atif_Aslam___Guitar__Baarishein_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =323)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Jibon_Re_Chords___Prem_Amar_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =324)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Ek_Galti_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =325)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notebook___Guitar__Nai_Lagda_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =326)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dilbar_Mere_Guitar_Chords___1982___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =327)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Do_Lafzon_Ki_Hai_Guitar_Chords___The_Great_Gambler___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =328)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mohit_Chauhan___Guitar__Kyun_Dil_Mera_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =329)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dhavni_Bhanushali__Leja_Leja_Re_Guitar_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =330)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Song_Nigam__Marham_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =331)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Band___Strings__Piya_Re_Guitar_Chords___Cornetto___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =332)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Naino_Ki_To_Baat_Chords___Mera_Sanam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =333)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phir_Se___Guitar__Maine_Socha_Ke_Chura_Loon_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =334)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Band___Strings__Mil_Gaya_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =335)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jass_Gujral__Aa_bhi_Ja_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =336)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Teri_Galliyan_Chords__Unplugged_Acoustic____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =337)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Armaan_Malik___Zikr_Chords_with_Intro_Tabs___Guitar__Amavas____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =338)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darshan_Raval__Bhula_Diya_Chords___Lyrics___Guitar__With_Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =339)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Amavas___Guitar__Dhadkan_Chords_by_Jubin_Nautiyal___Palak_Muchhal___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =340)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tu_Karde_Haan_Chords___Akhil__with___without_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =341)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dhvani_Bhanushali__Main_Teri_Hoon_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =342)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tum_Mere_Ho_Chords___Vivek_Singh__Pehchaan_Music____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =343)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tum_Aisi_Kyun_Ho_Chords___Hum_Chaar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =344)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Barf_Si_Tu_Pighal_Ja_Chords___Armaan_Malik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =345)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darshan_Raval__Ek_Ladki_Ko_Dekha_To_Aisa_Laga_Guitar_Chords__Reprise____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =346)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Bheege_Bheege_Chords___Ankit_Tiwari__Sunidhi_Chauhan__Amavas____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =347)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Why_Cheat_India___Guitar__Tu_Kitna_Kaamyaab_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =348)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Chaar___Guitar__Manmeet_Mere_Chords___Mohit_Chauhan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =349)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Khwaaish_Chords___Sajan_Patel___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =350)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Chehre_Chords___Harish_Verma__Punjabi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =351)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Kaise_Bhuloon_Chords___Gurnazar_Chattha___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =352)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Bairiya_Chords___Bombairiya___Arko___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =353)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Ye_Pyaar_Nahi_To_Kya_Hai_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =354)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tu_Na_Mera_Chords___Arjun_Kanungo___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =355)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Baarishein_Chords___Ankit_Rajput___Shivangi_Bhayana___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =356)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Fraud_Saiyaan___Guitar__Ishq_Ishq_Tera_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =357)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tanha_Hua_Chords___Zero___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =358)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Lae_Dooba_Chords___Aiyaary__w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =359)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Alvida_Alvida_Chords___Little_Boy___Sonu_Nigam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =360)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Toke_Chara_Chords___Jubin_Nautiyal___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =361)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Ann_Bann_Chords___Zero___Kunal_Ganjawala___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =362)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Jind_Mahi_Chords___Diljit_Dosanjh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =363)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Dil_Mein_Ho_Tum_Chords_by_Armaan_Malik___Why_Cheat_India___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =364)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Simmba__New_Tere_Bin_Guitar_Chords___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =365)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mahi_Aaja_Chords___Asim_Azhar_ft__Momina_Mustehsan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =366)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Behe_Chala_Chords___Yaseer_Desai__Shashwat_Sachdev___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =367)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Billian_Billian_Chords___Guri___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =368)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Why_Cheat_India__Phir_Mulaaqat_Chords___Guitar___Jubin_Nautiyal___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =369)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Fikar_Chords___Rahat_Fateh_Ali_Khan___Neha_Kakkar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =370)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Yasser_Desai___Tum_Chale_Gaye_Chords___Marudhar_Express___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =371)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Jo_Tu_Na_Mila_Chords___Asim_Azhar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =372)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Sakhiyaan_Chords___Maninder_Buttar___Babbu___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =373)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Teen_Cup_Chaa_Chords___Title_Track___Subho_Pramanik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =374)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Jaan_Nisaar_Chords__w_wo_Capo___Strumming____Kedarnath___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =375)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Soham_Naik___Tum_Aaoge_Chords__w_wo_Capo___Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =376)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mera_Pyar_Tera_Pyar_Chords__w_wo_Capo___Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =377)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tere_Te_Chords___Guru_Randhawa___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =378)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tu_Hi_Re_Chords___Armaan_Malik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =379)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Pinjra_Chords___Gurnazar__w_wo_Capo___Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =380)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mamla_Dil_Da_Chords___Tonny_Kakkar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =381)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bhaagte_Raho___Guitar__Gum_Hoon_Chords___Yasser_Desai___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =382)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Manush_Ekhono_Manusher_Pashe_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =383)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mujhe_Kaise_Pata_Na_Chala_Chords___Papon___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =384)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sweetheart_Guitar_Chords___Kedarnath___Dev_Negi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =385)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tere_Jisam_Chords_with_Strumming_Pattern___Altaaf_Sayyed___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =386)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Naina_Chords_by_Ankit_Tiwari___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =387)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Nazm_Nazm_Chords__Two_versions____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =388)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Meray_Saathiya_Chords___Roxen___Mustafa_Zahid___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =389)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tera_Yaar_Hoon_Main_Chords___Arijit_Singh__w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =390)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tu_Kareeb_Aaya_Chords___Rishabh_Srivastava___Aakanksha_Sharma___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =391)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Akhia_Di_Bhatkan_Chords___Sharry_Mann___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =392)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Sunn_Le_Zara_Chords___Arnab_Dutta___1921___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =393)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Allah_Duhai_Hai_Chords___Zayn___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =394)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Qaafirana_Chords_with_Strumming___Arijit_Singh___Kedarnath___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =395)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Sapna_Chords_with_Strumming_Pattern___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =396)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mere_Naam_Tu_Chords_with_Strumming_Pattern___Zero___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =397)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Aawargi_Chords_with_Strumming_Pattern___Jubin_Nautiyal___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =398)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mein_Adhura_Lafz_Chords_with_Strumming_Pattern___Baazaar___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =399)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Dil_Zaffran_Chords_with_Strumming_Pattern___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =400)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Pagal_Chords_by_Diljit_Dosanjh__Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =401)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Zindagi_Mil_Jayegi_Chords___Tony___Neha_Kakkar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =402)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Teri_Judai_Mein_Chords_by_Hukam_Ali___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =403)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Baaki_Hai_Chords_with_Strumming_Pattern___Sonu_Nigam___5_Weddings___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =404)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Siren_Chords_by_The_Chainsmokers___Aazar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =405)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__If_I_Say_Chords_by_Mumford___Sons___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =406)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Got_My_Name_Changed_Back_Chords___Pisot_Annies___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =407)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Namo_Namo_Chords___Kedarnath___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =408)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Baarish_Chords_by_Neha_Kakkar___Bilal_Saeed___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =409)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Dil_Mastiyaan_Chords___Ash_King___Payal_Dev___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =410)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Kya_Baat_Ay_Chords_with_Strumming_Pattern___Hardy_Sandhu___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =411)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bhaiji__Do_Naina_Chords_with_Strumming_Pattern___Yasser_Desai_Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =412)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Jaane_Ye_Kyun_Kiya_Chords_with_Strumming_Pattern___Farhan_Akhtar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =413)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Nain_Na_Jodi_Chords_with_Strumming_Pattern___Ayushmann_Khurrana___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =414)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh__Dooba_Dooba_Chords_with_Strumming_Pattern___Guitar__Helicopter_Eela____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =415)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def KK__Pehle_Ke_Jaisa_Chords_with_Strumming_Pattern___Jalebi_Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =416)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Iktara_Chords_with_Strumming_Pattern___Wake_Up_Sid___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =417)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Dooba_Dooba_Chords_by_Sanam_Puri___Silk_Route__Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =418)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Chhod_Diya_Chords_with_Strumming_Pattern___Baazaar___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =419)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Fakira_Chords_by_Gurnam_Bhullar___Qismat___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =420)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Soch_Na_Sake_Guitar_Chords_with_Strumming_Pattern___Airlift_Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =421)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atif__Tere_Liye_Chords_with_Strumming_Pattern___Guitar___Namaste_England___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =422)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh__Pal_Chords_with_Strumming_Pattern__Capo_Non_Capo____Guitar___Jalebi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =423)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh__Har_Har_Gange_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =424)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tum_Se_Chords_with_Strumming_Pattern__Capo____Jubin_Nautiyal_Jalebi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =425)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darshan_Raval__Do_Din_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =426)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Naina_Da_Kya_Kasoor_Chords_with_Strumming_Pattern___Andhadhun___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =427)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aap_Se_Milkar_Chords_with_Strumming_Pattern_Ayushmann_Khurrana___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =428)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Le_Ja_Tu_Kahin_Chords_with_Strumming_Pattern___Arijit_Singh_Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =429)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aye_Zindagi_Chords_with_Strumming_Pattern___Sonu_Nigam_Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =430)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit__Woh_Ladki_Chords_with_Strumming_Pattern___Andhadhun_Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =431)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Doorie_Chords_with_Strumming_Pattern___Benjamin_Rohan_Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =432)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mitron__Door_Na_Ja_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =433)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atif_Aslam__Tum_Chords_with_Strumming_Pattern___Laila_Majnu_Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =434)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jubin_Nautiyal___Sawarne_Lage_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =435)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def F_For_Fyaar_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =436)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy_Neele_Neele_Ambar_Par_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =437)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh___Aahista_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =438)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Nazar_Na_Lag_Jaaye_Chords_with_Strumming_Pattern___Guitar___Ash_King___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =439)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Promises_Chords_with_Strumming_Pattern___Guitar___Sam_Smith__Calvin_Harris___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =440)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sochta_Hoon___Dekhte_Dekhte_Chords___Guitar__with_Capo___without_Capo____Atif_Aslam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =441)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atif_Aslam___Chalte_Chalte_Chords_with_Strumming_Pattern__Easy____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =442)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanam_Puri___Bheegi_Bheegi_Raaton_Mein_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =443)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atif_Aslam_Tera_Hua_Chords_with_Strumming_Pattern___Loveratri___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =444)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Fanney_Khan___Tere_Jaisa_Tu_Chords_With_strumming_Pattern__Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =445)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhse_Naraz_Nahi_Zindagi_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =446)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hamza_Malik___O_Jaana_Chords_with_Strumming_Pattern_by_Rahat_Fateh_Ali_Khan___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =447)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atif_Aslam___Jeena_Jeena_Chords_with_Strumming_Pattern___Guitar___Badlapur___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =448)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar___Easy_Happy_Birthday_Chords_with_Strumming_Pattern__Multiple_Version____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =449)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def David_Guetta___Dont_Leave_Me_Alone_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =450)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh___Andheron_Mein_Rishtey_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =451)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Satyameva_Jayate___Tere_Jaisa_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =452)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sabrina_Claudio___Messages_From_Her_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =453)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kya_Hua_Tera_Wada_Chords_with_Strumming_Pattern___Guitar___Old_Song___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =454)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def 3_Idiots___Give_Me_Some_Sunshine_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =455)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chura_Liya_Hai_Tumne_Jo_Dil_Ko_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =456)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Samne_Wali_Khidki_Mein_Chords_with_Strumming_Pattern___Guitar___Old_Song___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =457)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gold___Naino_Ne_Baandhi_Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =458)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darshan_Raval___Baarish_Lete_Aana_Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =459)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Naino_Ne_Baandhi_Chords___Guitar___Mouni_Roy___Akshay_Kumar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =460)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_baar_Dhadak_Chords_With_Capo_and_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =461)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sunidhi_Chauhans_Mohabbat_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =462)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_Baar_Piano_Notes___Dhadak___Jhanvi_Kapoor___Ishaan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =463)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh___Tera_Fitoor_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =464)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dhadak___Pehli_Baar_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =465)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atif_Aslam___Paniyo_Sa_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =466)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Fanney_Khan___Halka_Halka_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =467)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Karwaan___Saansein_Chords_With_Strumming_Pattern___Guitar___Prateek_Khulad___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =468)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chori_Chori_Jab_Nazrein_Mili_Chords_With_Strumming_Pattern_Guitar___Namita___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =469)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darshan_Raval___Baarish_Lete_Aana_Chords_With_Strumming_Pattern___With_Without_Capo___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =470)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Asees_Zaroorat_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =471)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Janhvi_Kapoor___Dhadak_Title_Track_Chords___Guitar__First_Song____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =472)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def SANJU___Ruby_Ruby_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =473)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kyun_Na_Mere_Chords___Guitar___Rishabh_Srivastava___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =474)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kanth_Kaler___Silsila_Chords___Guitar__Punjabi_Song____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =475)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Param_Singh___Jhanjar_Chords___Guitar___Punjabi_Song___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =476)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Geeta_Zaildar___Jeen_Nu_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =477)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ahida_Chords___Guitar___Shyamoli_Singh__Ravi_Singhal___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =478)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kuch_Iss_Tarah_Chords_With_Strumming_Pattern___Guitar_1921___Zareen_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =479)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ayushmann_Khurrana___Chan_Kitthan_Chords_With_Strumming___Guitar____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =480)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Akhil___Rang_Gora_Chords_With_Strumming_Pattern___Guitar__Punjabi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =481)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Satyameva_Jayate___Dilbar_Chords___Guitar___Neha_Kakkar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =482)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baaghi_2___O_Saathi_Chords_Without_Capo__Guitar____Atif_Aslam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =483)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Papa_Kehte_Hain_Chords_With_Strumming___Qayamat_Se_Qayamat_Tak___Udit_Narayan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =484)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bhuvan_Bam___Safar_Guitar_Chords_With_Strumming_Pattern__BB_Ki_Vines____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =485)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guri___Jaan_Guitar_Chords___ALBUM_26___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =486)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kar_Har_Maidaan_Fateh_Chords___SANJU__With_Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =487)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Papon___Pakhi_Pakhi_Guitar_Chords_With_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =488)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baaghi_2___O_Saathi_Chords_With_Capo__Guitar____Atif_Aslam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =489)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gulabi_Aankhen_Chords_with_Guitar_Strumming_Pattern___Atif_Aslam_R_D_Burman___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =490)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sona_Mohapatra___Anhad_Naad_Guitar_Chords_With_Strumming_Pattern___Lal_Pari_Mastani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =491)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sonu_Nigam___Chaahaton_Ke_Saaye_Mein_Guitar_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =492)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Sapno_Ki_Rani_Guitar_Chords___Kishore_Kumar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =493)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arjun_Kanungo__Momina_Mustehsan___Aaya_Na_Tu_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =494)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Dua_Hai_Guitar_Chords___Tabs__Darshan_Raval___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =495)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar_Chords_of_Darasal___Atif_Aslam___Raabta__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =496)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rahul_Vaidya___Keh_Do_Na_Guitar_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =497)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def De_De_Jagah_Guitar_Chords_with_Strumming_Pattern___Parmanu___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =498)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gal_Sun_Jayein_Guitar_Chords___Akhil_Sachdeva__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =499)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pyar_Nai_Karna_Aya_Guitar_Chords___Karan_Juneja___Punjabi__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =500)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sare_Karo_Dab_Guitar_Chords___Sonu_Kakkar__Raftaar__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =501)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aa_Jao_Na_Guitar_Chords___Arijit_Singh___Veere_Di_Wedding__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =502)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jitni_Dafa_Guitar_Chords_From_Parmanu_With_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =503)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Meri_Aashiqui_Guitar_Chords___Balraj_With_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =504)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ghar_Se_Nikalte_Hi_Guitar_Chords___Armaan_Malik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =505)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def SANJU___Main_Badhiya_Tu_Bhi_Badhiya_Guitar_Chords_With_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =506)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Harsohena___Tere_Bin_Guitar_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =507)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Andra___Sudamericana_Guitar_Chords_With_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =508)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ae_Watan_Guitar_Chords___Arijit_Singh___Raazi__With_Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =509)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Selfish_Guitar_Chords___Atif_Aslam___Race_3__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =510)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Heeriye_Guitar_Chords_with_Intro_Tabs___Race_3___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =511)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Ghata_Guitar_Chords___Gajendra_Verma__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =512)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humnava_Mere_Guitar_Chords___Jubin_Nautiyal__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =513)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Diyan_Gallan_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =514)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Se_Teri_Guitar_Chords___Strumming_Pattern___Padman(request):
	text = Sargams.objects.filter(id__iexact =515)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanu_Ek_Pal_Chain_Guitar_Chords___Strumming_Pattern___Raid(request):
	text = Sargams.objects.filter(id__iexact =516)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lae_Dooba_Guitar_Chords___Strumming_Pattern___Aiyaary(request):
	text = Sargams.objects.filter(id__iexact =517)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_Saathi_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =518)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Yaar_Hoon_Main_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =519)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gazab_Ka_Hai_Din_Guitar_Chords___Strumming_Pattern___Dil_Juunglee(request):
	text = Sargams.objects.filter(id__iexact =520)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lo_Safar_Guitar_Chords___Strumming_Pattern___Baaghi_2(request):
	text = Sargams.objects.filter(id__iexact =521)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Meri_Khamoshi_Hai_Guitar_Chords___Strumming_Pattern___Pari(request):
	text = Sargams.objects.filter(id__iexact =522)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Theher_Ja_Guitar_Chords___Strumming_Pattern___October(request):
	text = Sargams.objects.filter(id__iexact =523)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Boond_Boond_Guitar_Chords___Strumming_Pattern___Hate_Story_4(request):
	text = Sargams.objects.filter(id__iexact =524)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_Ishq_Hai_Guitar_Chords___Strumming_Pattern___Rangoon___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =525)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Dil_Mein_Guitar_Chords___Strumming_Pattern___Armaan_Malik(request):
	text = Sargams.objects.filter(id__iexact =526)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def 25_Most_Romantic_Bollywood_Songs_Guitar_Chords_For_Valentine_Week(request):
	text = Sargams.objects.filter(id__iexact =527)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kho_Diya_Guitar_Chords___Strumming_Pattern___Bhoomi(request):
	text = Sargams.objects.filter(id__iexact =528)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Bina_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =529)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humsafar_Guitar_Chords___Strumming_Pattern___badrinath_ki_dulhania(request):
	text = Sargams.objects.filter(id__iexact =530)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Meet_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =531)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hawayein_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =532)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ghar_Guitar_Chords___Strumming_Pattern___Jab_Harry_Met_Sejal(request):
	text = Sargams.objects.filter(id__iexact =533)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Mere_Darmiyaan_Guitar_Chords___Strumming_Pattern___Chef(request):
	text = Sargams.objects.filter(id__iexact =534)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jaane_de_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =535)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Love_You_Zindagi_Guitar_Chords___Strumming_Pattern___Dear_Zindagi(request):
	text = Sargams.objects.filter(id__iexact =536)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Channa_Mereya_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =537)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def The_Humma_Song_Guitar_Chords___Strumming_Pattern___OK_Jaanu(request):
	text = Sargams.objects.filter(id__iexact =538)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Hi_Hai_Guitar_Chords___Strumming_Pattern___Dear_Zindagi(request):
	text = Sargams.objects.filter(id__iexact =539)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Nashe_Si_Chadh_Gayi_Guitar_Chords___Strumming_Pattern___Befikre(request):
	text = Sargams.objects.filter(id__iexact =540)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Enna_Sona_Guitar_Chords___Strumming_Pattern___OK_Jaanu(request):
	text = Sargams.objects.filter(id__iexact =541)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zaalima_Guitar_Chords___Strumming_Pattern___Raees(request):
	text = Sargams.objects.filter(id__iexact =542)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_Dafa_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =543)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bawara_Mann_Guitar_Chords___Strumming_Pattern___Jolly_LLB_2(request):
	text = Sargams.objects.filter(id__iexact =544)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Orrey_Mon_Guitar_Chords___Strumming_Pattern___Ayushmann_Khurrana(request):
	text = Sargams.objects.filter(id__iexact =545)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bulleya_Guitar_Chords___Strumming_Pattern___Ae_Dil_Hai_Mushkil(request):
	text = Sargams.objects.filter(id__iexact =546)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaabil_Hoon_Guitar_Chords___Strumming_Pattern___Kaabil(request):
	text = Sargams.objects.filter(id__iexact =547)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dariya_Guitar_Chords___Strumming_Pattern___Baar_Baar_Dekho(request):
	text = Sargams.objects.filter(id__iexact =548)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dhal_Jaun_Main_Guitar_Chords___Strumming_Pattern___Rustom(request):
	text = Sargams.objects.filter(id__iexact =549)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darkhaast_Guitar_Chords___Strumming_Pattern___Shivaay(request):
	text = Sargams.objects.filter(id__iexact =550)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Toota_Jo_Kabhi_Tara_Guitar_Chords___Strumming___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =551)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kho_Gaye_Hum_Kahan_Guitar_Chords___Strumming___Baar_Baar_Dekho(request):
	text = Sargams.objects.filter(id__iexact =552)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Besabriyaan_Guitar_chords___Strumming_Pattern___M_S_Dhoni(request):
	text = Sargams.objects.filter(id__iexact =553)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ae_Dil_Hai_Mushkil_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =554)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sau_Aasmaan_Guitar_Chords___Strumming_Pattern___Baar_Baar_Dekho(request):
	text = Sargams.objects.filter(id__iexact =555)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Raaz_Aankhein_Teri_Guitar_Chords___Strumming_Pattern___Raaz_Reboot(request):
	text = Sargams.objects.filter(id__iexact =556)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yaad_Hai_Na_Guitar_Chords___Strumming_Pattern___Raaz_Reboot(request):
	text = Sargams.objects.filter(id__iexact =557)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phir_Kabhi_Guitar_Chords___Strumming_Pattern___M_S_Dhoni(request):
	text = Sargams.objects.filter(id__iexact =558)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jaago_Guitar_chords___Strumming_Pattern___Rock_on_2(request):
	text = Sargams.objects.filter(id__iexact =559)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aadat_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =560)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zara_Si_Dosti_Guitar_Chords___Strumming_Pattern___Happy_Bhag_Jayegi(request):
	text = Sargams.objects.filter(id__iexact =561)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kuch_Toh_Hai_Guitar_Chords___Strumming_Pattern___Do_Lafzon_Ki_Kahani(request):
	text = Sargams.objects.filter(id__iexact =562)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mujhko_Barsaat_Bana_Lo_Guitar_Chords___Strumming_Pattern___Junooniyat(request):
	text = Sargams.objects.filter(id__iexact =563)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pani_Da_Rang_Guitar_Chords___Strumming_Pattern___Vicky_Donor(request):
	text = Sargams.objects.filter(id__iexact =564)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Alvida_Guitar_Chords___Strumming_Pattern___Traffic(request):
	text = Sargams.objects.filter(id__iexact =565)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ishqe_Di_Lat_Guitar_Chords___Strumming_Pattern___Junooniyat(request):
	text = Sargams.objects.filter(id__iexact =566)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ikk_Kudi_Guitar_Chords___Strumming_Pattern___Udta_Punjab(request):
	text = Sargams.objects.filter(id__iexact =567)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mile_Ho_Tum_Humko_Guitar_Chords___Strumming_Pattern___Fever(request):
	text = Sargams.objects.filter(id__iexact =568)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Yaad_Guitar_Chords___Strumming_Pattern___Fever(request):
	text = Sargams.objects.filter(id__iexact =569)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Sang_Yaara_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =570)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dekha_Hazaro_Dafaa_Guitar_Chords___Strumming_Pattern___Rustom(request):
	text = Sargams.objects.filter(id__iexact =571)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Le_Chala_Guitar_Chords___Strumming_Pattern___One_Night_Stand(request):
	text = Sargams.objects.filter(id__iexact =572)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ijazat_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =573)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Awargi_Guitar_Chords___Strumming_Pattern___Love_Games(request):
	text = Sargams.objects.filter(id__iexact =574)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Itni_Si_Baat_Hai_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =575)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bol_Do_Na_Zara_Guitar_Chords___Strumming_Pattern___Azhar(request):
	text = Sargams.objects.filter(id__iexact =576)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Girl_I_Need_You_Guitar_Chords___Strumming_Pattern___Baaghi(request):
	text = Sargams.objects.filter(id__iexact =577)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aafreen_Guitar_Chords___Strumming_Pattern___1920_London(request):
	text = Sargams.objects.filter(id__iexact =578)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rootha_Kyun_Guitar_Chords___Strumming_Pattern___1920_London(request):
	text = Sargams.objects.filter(id__iexact =579)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_Nazar_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =580)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Salamat_Guitar_Chords___Strumming_Pattern___Sarbjit(request):
	text = Sargams.objects.filter(id__iexact =581)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehla_Nasha_Guitar_Chords___Strumming_Pattern___Amir_Khan(request):
	text = Sargams.objects.filter(id__iexact =582)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zara_Sa_Guitar_Chords___Strumming_Pattern___Jannat(request):
	text = Sargams.objects.filter(id__iexact =583)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Woh_Chaand_Guitar_Chords___Strumming___Teraa_Surroor(request):
	text = Sargams.objects.filter(id__iexact =584)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Chehra_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =585)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Manwa_Behrupiya_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =586)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bolna_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =587)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bekhudi_Guitar_Chords___Strumming_Pattern___Teraa_Surroor(request):
	text = Sargams.objects.filter(id__iexact =588)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Mere_Paas_Guitar_Chords___Strumming_Pattern___Wazir(request):
	text = Sargams.objects.filter(id__iexact =589)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gazab_Ka_Hai_Ye_Din_Guitar_Chords___Strumming_Pattern___Sanam_Re(request):
	text = Sargams.objects.filter(id__iexact =590)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rehnuma_Guitar_Chords___Strumming_Pattern___Rocky_Handsome(request):
	text = Sargams.objects.filter(id__iexact =591)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ji_Huzoori_Guitar_Chords___Strumming_pattern___Ki_And_Ka(request):
	text = Sargams.objects.filter(id__iexact =592)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sab_Tera_Guitar_Chords___Strumming_Pattern___Baaghi(request):
	text = Sargams.objects.filter(id__iexact =593)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Wafa_Ne_Bewafai_Guitar_Chords___Strumming_Pattern___Teraa_Surroor(request):
	text = Sargams.objects.filter(id__iexact =594)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Agar_Tu_Hota_Guitar_Chords___Strumming_Pattern___Baaghi(request):
	text = Sargams.objects.filter(id__iexact =595)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Soch_Na_Sake_Guitar_Chords___Strumming_Pattern___Airlift(request):
	text = Sargams.objects.filter(id__iexact =596)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumhe_Apna_Banane_ka_Junoon_Guitar_Chords___Strumming_Pattern___Hate_Story_3(request):
	text = Sargams.objects.filter(id__iexact =597)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gerua_Guitar_Chords___Strumming_Pattern___Dilwale(request):
	text = Sargams.objects.filter(id__iexact =598)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Safarnama_Guitar_Chords___Strumming_Pattern___Tamasha(request):
	text = Sargams.objects.filter(id__iexact =599)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mar_Jaayen_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =600)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Janam_Janam_Guitar_Chords___Strumming_Pattern___Dilwale(request):
	text = Sargams.objects.filter(id__iexact =601)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sathia_Guitar_Chords___Strumming_Pattern___Ankit_Tiwari(request):
	text = Sargams.objects.filter(id__iexact =602)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yeh_Fitoor_Mera_Guitar_Chords___Strumming_Pattern___Fitoor(request):
	text = Sargams.objects.filter(id__iexact =603)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanam_Re_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =604)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atrangi_Yaari_Guitar_Chords___Strumming_Pattern___Wazir(request):
	text = Sargams.objects.filter(id__iexact =605)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bandeya_Guitar_Chords___Strumming_Pattern___Jazbaa(request):
	text = Sargams.objects.filter(id__iexact =606)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Nazdeekiyan_Guitar_Chords___Strumming_Pattern___Shaandaar(request):
	text = Sargams.objects.filter(id__iexact =607)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Woh_Dekhne_Me_Guitar_Chords___Strumming_Pattern___Ali_Zafar(request):
	text = Sargams.objects.filter(id__iexact =608)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lukka_Chuppi_Guitar_Chords___Strumming_Pattern___Rang_De_Basanti(request):
	text = Sargams.objects.filter(id__iexact =609)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zara_Zara_Guitar_Chords___Strumming_Pattern___RHTDM(request):
	text = Sargams.objects.filter(id__iexact =610)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Moora_Guitar_Chords___Strumming_Pattern___Gangs_Of_Wasseypur_2(request):
	text = Sargams.objects.filter(id__iexact =611)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Awari_Guitar_Chords___Strumming_Pattern___Ek_Villain(request):
	text = Sargams.objects.filter(id__iexact =612)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Iss_Qadar_Pyar_Hai_Guitar_Chords___Strumming_Pattern___Bhaag_Johnny(request):
	text = Sargams.objects.filter(id__iexact =613)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Be_Intehaan_Guitar_Chords___Strumming_Pattern___Race_2(request):
	text = Sargams.objects.filter(id__iexact =614)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Khoya_Khoya_Guitar_Chords___Strumming_Pattern___Hero(request):
	text = Sargams.objects.filter(id__iexact =615)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sau_Aasoon_Guitar_Chords___Strumming_Pattern___Katti_Batti(request):
	text = Sargams.objects.filter(id__iexact =616)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def _Rock__Khwaishein_Guitar_Chords___Strumming_Pattern___Calender_Girls(request):
	text = Sargams.objects.filter(id__iexact =617)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Khwaishein_Guitar_Chords___Strumming_Pattern___Calender_Girls(request):
	text = Sargams.objects.filter(id__iexact =618)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Woh_Lamhe_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =619)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Roobaroo_Guitar_Chords___Strumming_Pattern___Rang_De_Basanti(request):
	text = Sargams.objects.filter(id__iexact =620)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hona_Tha_Pyar_Guitar_chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =621)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bhaag_Dk_Bose_Guitar_Chords___Strumming_Pattern___Delhi_Belly(request):
	text = Sargams.objects.filter(id__iexact =622)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chal_Chale_Apne_Ghar_Guitar_Chords___Strumming_Pattern___Woh_Lamhe(request):
	text = Sargams.objects.filter(id__iexact =623)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hai_Koi_Guitar_Chords___Strumming_Pattern___Gajendra_Verma(request):
	text = Sargams.objects.filter(id__iexact =624)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phoolon_Ka_Taaro_Ka_Guitar_Chords___Strumming_Pattern___Raksha_Bandhan(request):
	text = Sargams.objects.filter(id__iexact =625)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yaaron_Dosti_Guitar_Chords___Strumming_Pattern___Kk(request):
	text = Sargams.objects.filter(id__iexact =626)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Jo_Mila_Guitar_Chords___Strumming_Pattern___Bajrangi_Bhaijaan(request):
	text = Sargams.objects.filter(id__iexact =627)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zehnaseeb_Guitar_Chords___Strumming_Pattern___Hasee_Toh_Phasee(request):
	text = Sargams.objects.filter(id__iexact =628)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Na_Jaane_Aas_Pass_Hai_Khuda_Guitar_Chords___Strumming_Pattern(request):
	text = Sargams.objects.filter(id__iexact =629)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Hoon_Hero_Tera_Guitar_Chords___Strumming_Pattern___Hero(request):
	text = Sargams.objects.filter(id__iexact =630)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ove_Janiya_Guitar_Chords___Strumming_Pattern___Katti_Batti(request):
	text = Sargams.objects.filter(id__iexact =631)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Banjarey_Guitar_Chords___Strumming_Pattern_By_Honey_Singh___Fugly(request):
	text = Sargams.objects.filter(id__iexact =632)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Galliyan_Guitar_Chords___Strumming_Pattern___Ek_Villian(request):
	text = Sargams.objects.filter(id__iexact =633)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Hi_Ho_Guitar_Chords___Strumming_Pattern_By_Arijit_Singh___Aashiqui_2(request):
	text = Sargams.objects.filter(id__iexact =634)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ilahi_Guitar_Chords___Strumming_Pattern_by_Arijit_Singh___Yeh_Jawaani_Hai_Deewani(request):
	text = Sargams.objects.filter(id__iexact =635)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_Baar_Guitar_Chords___Strumming_Pattern___Dil_Dhadakne_Do(request):
	text = Sargams.objects.filter(id__iexact =636)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ambarsariya_Guitar_Chords___Strumming_Pattern___Fukrey(request):
	text = Sargams.objects.filter(id__iexact =637)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Ho_Toh_Guitar_Chords___Strumming_Pattern___Rock_On(request):
	text = Sargams.objects.filter(id__iexact =638)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pichle_Saat_Dino_Me_Guitar_Chords___Strumming_Pattern___Rock_On(request):
	text = Sargams.objects.filter(id__iexact =639)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saware_Guitar_Chords___Strumming_Pattern_By_Arijit_Singh___Phantom(request):
	text = Sargams.objects.filter(id__iexact =640)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Give_Me_Some_Sunshine_Guitar_Chords___Strumming_Pattern__3_Idiots(request):
	text = Sargams.objects.filter(id__iexact =641)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabira_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =642)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Chahiye_Guitar_Chords___Strumming_Pattern___Bajrangi_Bhaijaan(request):
	text = Sargams.objects.filter(id__iexact =643)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jhoom_Guitar_Chords__Strumming_Pattern___Ali_Zafar(request):
	text = Sargams.objects.filter(id__iexact =644)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hamari_Adhuri_Kahani_Guitar_Chords___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =645)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hasi_Ban_Gaye_Guitar_Chords___Hamari_Adhuri_Kahani(request):
	text = Sargams.objects.filter(id__iexact =646)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gulabi_Aankhen_Atif_Aslam_Guitar_Chords___Strumming_Pattern(request):
	text = Sargams.objects.filter(id__iexact =647)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jeena_Jeena_Guitar_Chords___Atif_Aslam_Badlapur(request):
	text = Sargams.objects.filter(id__iexact =648)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kuch_Bhi_Karlo_Guitar_Chords___Swastik_the_Band(request):
	text = Sargams.objects.filter(id__iexact =649)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chal_Chale_Apne_Ghar_Guitar_Chords___Strumming_Pattern___Woh_Lamhe(request):
	text = Sargams.objects.filter(id__iexact =650)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dekha_Hazaro_Dafaa_Guitar_Chords___Strumming_Pattern___Rustom(request):
	text = Sargams.objects.filter(id__iexact =651)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bolna_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =652)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Soch_Na_Sake_Guitar_Chords___Strumming_Pattern___Airlift(request):
	text = Sargams.objects.filter(id__iexact =653)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Rahoon_Ya_Na_Rahoon_Guitar_Chords___Emraan_Hashmi(request):
	text = Sargams.objects.filter(id__iexact =654)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumhe_Apna_Banane_ka_Junoon_Guitar_Chords___Strumming_Pattern___Hate_Story_3(request):
	text = Sargams.objects.filter(id__iexact =655)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zara_Sa_Guitar_Chords___Strumming_Pattern___Jannat(request):
	text = Sargams.objects.filter(id__iexact =656)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Iss_Qadar_Pyar_Hai_Guitar_Chords___Strumming_Pattern___Bhaag_Johnny(request):
	text = Sargams.objects.filter(id__iexact =657)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Hoon_Hero_Tera_Guitar_Chords___Strumming_Pattern___Hero(request):
	text = Sargams.objects.filter(id__iexact =658)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Sang_Yaara_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =659)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Hi_Ho_Guitar_Chords___Strumming_Pattern_By_Arijit_Singh___Aashiqui_2(request):
	text = Sargams.objects.filter(id__iexact =660)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jeena_Jeena_Guitar_Chords___Atif_Aslam_Badlapur(request):
	text = Sargams.objects.filter(id__iexact =661)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zehnaseeb_Guitar_Chords___Strumming_Pattern___Hasee_Toh_Phasee(request):
	text = Sargams.objects.filter(id__iexact =662)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jhoom_Guitar_Chords__Strumming_Pattern___Ali_Zafar(request):
	text = Sargams.objects.filter(id__iexact =663)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Be_Intehaan_Guitar_Chords___Strumming_Pattern___Race_2(request):
	text = Sargams.objects.filter(id__iexact =664)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Meri_Kahani_Guitar_Chords___Strumming_Pattern___BB_Ki_Vines(request):
	text = Sargams.objects.filter(id__iexact =665)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phir_Kabhi_Guitar_Chords___Strumming_Pattern___M_S_Dhoni(request):
	text = Sargams.objects.filter(id__iexact =666)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_Nazar_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =667)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darkhaast_Guitar_Chords___Strumming_Pattern___Shivaay(request):
	text = Sargams.objects.filter(id__iexact =668)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kho_Diya_Guitar_Chords___Strumming_Pattern___Bhoomi(request):
	text = Sargams.objects.filter(id__iexact =669)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Meet_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =670)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humsafar_Guitar_Chords___Strumming_Pattern___badrinath_ki_dulhania(request):
	text = Sargams.objects.filter(id__iexact =671)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sang_Hoon_Tere_Guitar_Chords___Strumming_Pattern___Bhuvan_Bam(request):
	text = Sargams.objects.filter(id__iexact =672)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hawayein_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =673)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Diyan_Gallan_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =674)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Se_Teri_Guitar_Chords___Strumming_Pattern___Padman(request):
	text = Sargams.objects.filter(id__iexact =675)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Vance_Joy___Riptide_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =676)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Judy_Garland___Somewhere_Over_The_Rainbow___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =677)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def John_Legend___All_Of_Me_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =678)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lukas_Graham___7_Years_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =679)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ruth_B___Lost_Boy_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =680)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def The_Chainsmokers___Closer_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =681)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Plain_White_Ts___Hey_There_Delilah_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =682)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Justin_Bieber___Love_Yourself_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =683)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Simon_And_Garfunkel___The_Sound_Of_Silence_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =684)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Oasis___Wonderwall_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =685)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jason_Mraz___Im_Yours_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =686)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def James_Bay___Let_It_Go_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =687)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hillsong_United___Oceans_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =688)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ed_Sheeran___Thinking_Out_Loud_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =689)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bon_Iver___Skinny_Love_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =690)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Beatles___Hey_Jude_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =691)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Adele___Someone_Like_You_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =692)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Eagles___Hotel_California_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =693)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jeff_Buckley___Hallelujah_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =694)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ed_Sheeran___Photograph_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =695)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumhe_Apna_Banane_Ka_Guitar_Tabs___Lead___Hate_Story_3___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =1)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chaar_Kadam_Guitar_Tabs___Lead___PK_2014____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =2)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Phir_Tumpe_Pyar_Aaya_Hai_Guitar_Tabs___Lead___Hate_Story_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =3)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Chahiye_Guitar_Tabs___Lead___Bajrangi_Bhaijaan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =4)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kya_Mujhe_Pyar_Hai_Guitar_Tabs___Lead___Woh_Lamhe___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =5)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def BAARISH_Guitar_Tabs___Lead___Yaariyan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =6)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Aaj_Kal_Guitar_Tabs___Lead___Purani_Jeans___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =7)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def HUMDARD_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =8)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Mar_Jayenge__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =9)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saanson_Ko_Jeene_Ka_Guitar_Tabs___Lead___Zid__2014____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =10)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Share_a_link_on_Twitter(request):
	text = Sargams.objects.filter(id__iexact =11)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Meri_Teri_Meri_Guitar_Tabs___Lead___Bodygaurd___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =12)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lag_Ja_Gale_Guitar_Tabs___Lead___Woh_Kaun_Thi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =13)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Muskurane_Ki_Wajah_Tum_Ho_Guitar_Tabs___Lead___City_Lights___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =14)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bin_Tere__Reprise__Guitar_Tabs___Lead___I_Hate_Love_Stories___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =15)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Iktara_Guitar_Tabs___Lead___Wake_Up_Sid___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =16)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Luka_Chuppi_Bahut_Huyi_Guitar_Tabs___Lead___Rang_De_Basanti___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =17)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Muskurane_Ki_Wajah_Tum_Ho_Guitar_Tabs___Lead___City_Lights___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =18)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Iktara_Guitar_Tabs___Lead___Wake_Up_Sid___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =19)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Dil_Shayrana_Guitar_Tabs___Lead___Holiday___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =20)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Galliyan_Teri_Galiyan_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =21)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Rang_Sharbaton_Ka__Phata_Poster_Nikla_Hero__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =22)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humnava_Guitar_Tabs___Lead___Humari_Adhuri_Kahani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =23)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rehnuma_Guitar_Tabs___Lead___ROCKY_HANDSOME___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =24)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Naam_Hamne_kiya_hai_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =25)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sun_Raha_Hai_na_tu__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =26)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaise_Mujhe_Tum_Mil_Gayi_Guitar_Tabs___Lead___Ghajini___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =27)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Mehboob_Qayamat_Hogi_Guitar_Tabs___Lead___Mr_X_In_Bombay___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =28)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aashiyan_Guitar_tabs__Barfi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =29)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Hi_Tu_Har_Jagah_Guitar_Tabs___Lead___KICK__2014____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =30)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Ladki_Ko_Dekha_To_Aisa_Laga_Guitar_Tabs___Lead___1942_Love_Story___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =31)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Hone_Laga_Hoon_Guitar_Tabs___Lead___Ajab_Prem_Ki_Ghazab_Kahani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =32)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humko_Humise_Chura_Lo_Guitar_Tabs___Lead___Mohabbatein_Tune___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =33)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Neele_Neele_Ambar_Par_Guitar_Tabs___Lead___Kalakaar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =34)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dheere_Dheere_Se_Guitar_Tabs___Lead___Aashiqui__1990____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =35)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def PANI_DA_RANG_vekh_ke_Guitar_Tabs___Lead___Vicky_Donor___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =36)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Re_Kabira_maan_jaa_Guitar_Tabs___Lead__Yeh_Jawaani_Hai_Deewani____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =37)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Paas_Aaye_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =38)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Agar_Tum_Saath_Ho_Guitar_Tabs___Lead___Tamasha___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =39)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehla_Nasha_Pehla_Hummar_Guitar_Tabs___Lead___Jo_Jeeta_Wohi_Sikandar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =40)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Chehra_Guitar_Tabs___Lead___SANAM_TERI_KASAM___ARIJIT_SINGH___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =41)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chura_Liya_Hai_Tumne_Jo_Dil_Ko_Guitar_Tabs___Lead___Yaadon_Ki_Baarat___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =42)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baatein_Ye_Kabhi_Na_Guitar_Tabs___Lead___Khamoshiyan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =43)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kal_Ho_Naa_Ho_Guitar_Tabs___Lead___Title_Track___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =44)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_Pehli_Baar_Mohabbat_Ki_Hai_Guitar_Tabs___Lead___Sirf_Tum___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =45)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_O_Jaane_Jaana_Guitar_Tabs___Lead___Pyar_Kiya_To_Darna_Kya___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =46)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Haseena_Thi_Ek_Deewana_Tha_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =47)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gulabi_Aankhein_Jo_Teri_Dekhi_Guitar_Tabs___Lead___The_Train___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =48)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hua_Hai_Aaj_Pehli_Baar_Guitar_Tabs___Lead___Sanam_Re___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =49)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Raabta_Guitar_Tabs___Lead___Agent_Vinod___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =50)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bolna_Guitar_Tabs___Lead____Kapoor_and_Sons__Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =51)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gerua_Guitar_Tabs___lead___Dilwale__2015____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =52)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Rahoon_Ya_Na_Rahoon_Guitar_Tabs___Lead___Armaan_Malik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =53)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Hoon_Hero_Tera_Guitar_Tabs___Lead___Hero__Salman_Khan____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =54)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chahun_Main_Ya_Na__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =55)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def JEENA_JEENA_Guitar_Tabs___Lead___Badlapur__Atif_Aslam____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =56)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhe_Dekha_To_Ye_Jaana_Sanam_Guitar_Tabs___Lead___DDLJ_Tune___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =57)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabhi_Jo_Baadal_Barse_Guitar_Tabs___Lead__Jackpot____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =58)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Tenu_Samjhawan_Ki_Guitar_Tabs___Lead___Humpty_Sharma_Ki_Dulhania___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =59)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanam_Re_Guitar_Tabs___Lead___Sanam_Re__Arijit_Singh____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =60)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ishq_Wala_Love_Guitar_Tabs___Lead___Student_of_the_Year__SOTY____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =61)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_hi_ho__Ashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =62)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Soch_Na_Sake_Guitar_Tabs___Lead___Airlift__Arijit_Singh____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =63)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Janam_Janam_Guitar_Tabs___Lead___Dilwale__2015____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =64)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def List_of_Best_Bollywood_Guitar_Songs_of_all_the_time___Best_Hindi_Songs__2015____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =65)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Hoon_Hero_Tera_Guitar_Tabs___Lead___Hero__Salman_Khan____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =66)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Rahoon_Ya_Na_Rahoon_Guitar_Tabs___Lead___Armaan_Malik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =67)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumhe_Apna_Banane_Ka_Guitar_Tabs___Lead___Hate_Story_3___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =68)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Agar_Tum_Saath_Ho_Guitar_Tabs___Lead___Tamasha___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =69)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gerua_Guitar_Tabs___lead___Dilwale__2015____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =70)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Janam_Janam_Guitar_Tabs___Lead___Dilwale__2015____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =71)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanam_Re_Guitar_Tabs___Lead___Sanam_Re__Arijit_Singh____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =72)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Soch_Na_Sake_Guitar_Tabs___Lead___Airlift__Arijit_Singh____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =73)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hua_Hai_Aaj_Pehli_Baar_Guitar_Tabs___Lead___Sanam_Re___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =74)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabhi_Jo_Baadal_Barse_Guitar_Tabs___Lead__Jackpot____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =75)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Meri_Maa_Mumma_Guitar_Tabs___Lead___Kailash_Kher__Dasvidaniya____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =76)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saathiya_Pagle_Se_Dil_Ne_Ye_Kya_Kiya_Guitar_Tabs___Lead___Singham___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =77)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chhoti_Si_Pyari_Si_Nanhi_Si_Guitar_Tabs___Lead___Anari___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =78)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aashiyan_Guitar_tabs__Barfi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =79)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phoolon_Sa_Chehra_Tera_Guitar_Tabs___Lead___Anari___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =80)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_hi_ho__Ashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =81)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Rang_Sharbaton_Ka__Phata_Poster_Nikla_Hero__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =82)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sun_Raha_Hai_na_tu__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =83)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chahun_Main_Ya_Na__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =84)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aashiqui_2_love_theme_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =85)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Mar_Jayenge__Aashiqui_2__Guitar_Tabs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =86)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh_Guitar_Tabs___Lead___Best_of_Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =87)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ashiqui_2_Movie_Guitar_Tabs___Lead___All_Songs_of_Ashiqui_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =88)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Re_Kabira_maan_jaa_Guitar_Tabs___Lead__Yeh_Jawaani_Hai_Deewani____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =89)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhe_Dekha_To_Ye_Jaana_Sanam_Guitar_Tabs___Lead___DDLJ_Tune___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =90)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_O_Jaane_Jaana_Guitar_Tabs___Lead___Pyar_Kiya_To_Darna_Kya___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =91)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gulabi_Aankhein_Jo_Teri_Dekhi_Guitar_Tabs___Lead___The_Train___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =92)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Iktara_Guitar_Tabs___Lead___Wake_Up_Sid___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =93)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Paas_Aaye_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =94)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Naam_Hamne_kiya_hai_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =95)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def BAARISH_Guitar_Tabs___Lead___Yaariyan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =96)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Haseena_Thi_Ek_Deewana_Tha_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =97)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def PANI_DA_RANG_vekh_ke_Guitar_Tabs___Lead___Vicky_Donor___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =98)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehla_Nasha_Pehla_Hummar_Guitar_Tabs___Lead___Jo_Jeeta_Wohi_Sikandar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =99)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Naina_Maar_Hi_Daalenge_Guitar_tabs___Jai_Ho___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =100)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Aaj_Kal_Guitar_Tabs___Lead___Purani_Jeans___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =101)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kyon_na_hum_tum_Guitar_Tabs__Barfi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =102)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Mehboob_Qayamat_Hogi_Guitar_Tabs___Lead___Mr_X_In_Bombay___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =103)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Raabta_Guitar_Tabs___Lead___Agent_Vinod___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =104)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Galliyan_Teri_Galiyan_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =105)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def TU_HI_HAI_AASHIQUI_Guitar_Tabs___Dishkiyaoon___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =106)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Khali_Salam_Dua_Guitar_Tabs___Shortcut_Romeo___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =107)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Muskurane_Ki_Wajah_Tum_Ho_Guitar_Tabs___Lead___City_Lights___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =108)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Suno_Na_Sangemarmar_Guitar_Tabs___Youngistaan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =109)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humko_Humise_Chura_Lo_Guitar_Tabs___Lead___Mohabbatein_Tune___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =110)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kal_Ho_Naa_Ho_Guitar_Tabs___Lead___Title_Track___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =111)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Phir_Tumpe_Pyar_Aaya_Hai_Guitar_Tabs___Lead___Hate_Story_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =112)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Tenu_Samjhawan_Ki_Guitar_Tabs___Lead___Humpty_Sharma_Ki_Dulhania___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =113)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Dil_Shayrana_Guitar_Tabs___Lead___Holiday___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =114)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Meri_Teri_Meri_Guitar_Tabs___Lead___Bodygaurd___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =115)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chura_Liya_Hai_Tumne_Jo_Dil_Ko_Guitar_Tabs___Lead___Yaadon_Ki_Baarat___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =116)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Luka_Chuppi_Bahut_Huyi_Guitar_Tabs___Lead___Rang_De_Basanti___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =117)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Papa_Kehte_Hain_Bada_Naam_Karega_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =118)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Dil_Ki_Dhadkan_Mein_Guitar_Tabs___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =119)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dard_Dilo_Ke_Guitar_Tabs___Lead___The_Xpose___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =120)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Banjara_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =121)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def HUMDARD_Guitar_Tabs___Lead___Ek_Villain___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =122)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ishq_Wala_Love_Guitar_Tabs___Lead___Student_of_the_Year__SOTY____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =123)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Hi_Tu_Har_Jagah_Guitar_Tabs___Lead___KICK__2014____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =124)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sandese_Aate_Hain_Guitar_Tabs___Lead___Border___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =125)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Happy_Birthday_To_You_Guitar_Tabs___Lead___Bday_Song_Tune___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =126)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Raghupati_Raghav_Raja_Ram_Guitar_Tabs___Lead___Ram_Bhajan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =127)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Hone_Laga_Hoon_Guitar_Tabs___Lead___Ajab_Prem_Ki_Ghazab_Kahani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =128)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaise_Mujhe_Tum_Mil_Gayi_Guitar_Tabs___Lead___Ghajini___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =129)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hai_Dil_Ye_Mera_Guitar_Tabs___Lead___Hate_Story_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =130)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jumme_Ki_Raat_Hai_Guitar_Tabs___Lead___Kick__2014____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =131)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Naam_Doon_Guitar_Tabs___Lead___Its_Entertainment___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =132)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabhi_Aayine_Pe_Guitar_Tabs___Lead__Aye_Khuda____Hate_Story_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =133)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sawan_Aaya_Hai_Guitar_Tabs___Lead___Creature_3D___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =134)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sukoon_Mila_Guitar_Tabs___Lead___Mary_Kom___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =135)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gulaabi_Aankhen_Jo_Teri_Dekhi_Guitar_Chords___The_Train__1970____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =136)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Papa_kehte_hain_bada_naam_karega_Guitar_Chords___Qayamat_Se_Qayamat_Tak___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =137)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mera_Mann_Kehne_Laga_Guitar_Tabs___Lead___Nautanki_Saala___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =138)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Khushnuma_Guitar_Tabs___Lead___Suyyash_Rai___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =139)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saanson_Ko_Jeene_Ka_Guitar_Tabs___Lead___Zid__2014____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =140)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chaar_Kadam_Guitar_Tabs___Lead___PK_2014____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =141)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Are_Re_Are_Ye_Kya_Hua_Guitar_Tabs___Lead___Dil_To_Pagal_Hai___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =142)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Raja_Ko_Rani_Se_Pyaar_Ho_Gaya_Guitar_Tabs___Lead___Akele_Hum_Akele_Tum___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =143)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lag_Ja_Gale_Guitar_Tabs___Lead___Woh_Kaun_Thi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =144)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Wo_Lamhe_Wo_baatein_Guitar_Tabs___Lead___Atif_Aslam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =145)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bin_Tere__Reprise__Guitar_Tabs___Lead___I_Hate_Love_Stories___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =146)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bikhra_Hoon_Main_Guitar_Tabs___Lead___Aadat__Jal_The_Band____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =147)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baatein_Ye_Kabhi_Na_Guitar_Tabs___Lead___Khamoshiyan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =148)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kya_Mujhe_Pyar_Hai_Guitar_Tabs___Lead___Woh_Lamhe___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =149)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def JEENA_JEENA_Guitar_Tabs___Lead___Badlapur__Atif_Aslam____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =150)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_Pehli_Baar_Mohabbat_Ki_Hai_Guitar_Tabs___Lead___Sirf_Tum___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =151)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mitti_di_khushboo_Guitar_Tabs___Lead___Ayushmann_Khurrana___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =152)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dheere_Dheere_Se_Guitar_Tabs___Lead___Aashiqui__1990____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =153)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ek_Ladki_Ko_Dekha_To_Aisa_Laga_Guitar_Tabs___Lead___1942_Love_Story___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =154)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Doorie_Sahi_Jaye_Na_Guitar_Tabs___Lead___Atif_Aslam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =155)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Laila_Tu_Saamne_Kyun_Na_Aaye_Guitar_Tabs___Lead___Faridkot___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =156)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sooraj_Dooba_Hai_Yaaron_Guitar_Tabs___Lead___Roy___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =157)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Chahiye_Guitar_Tabs___Lead___Bajrangi_Bhaijaan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =158)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sawan_Ka_Mahina_Pawan_Kare_Guitar_Tabs___Lead___Milan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =159)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yaaron_Dosti_Badi_Hi_Haseen_Hai_Guitar_Tabs___Lead___k_k___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =160)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humnava_Guitar_Tabs___Lead___Humari_Adhuri_Kahani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =161)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Leke_Pehla_Pehla_Pyaar_Guitar_Tabs___Lead___CID__1956____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =162)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Saamne_Wali_Khidki_Mein_Guitar_Tabs___Lead___Padosan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =163)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Agar_Tum_Mil_Jao_Guitar_Tabs___Lead___Zeher___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =164)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sajda_Guitar_Tabs___Lead___My_Name_Is_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =165)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Neele_Neele_Ambar_Par_Guitar_Tabs___Lead___Kalakaar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =166)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Naina_Tere_Naina_Guitar_Tabs___Lead___My_Name_Is_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =167)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Chehra_Guitar_Tabs___Lead___SANAM_TERI_KASAM___ARIJIT_SINGH___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =168)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Meri_Kahaani_Guitar_Tabs___Lead___Gabbar_is_Back___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =169)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chunar_Guitar_Tabs___Lead___ABCD_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =170)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bolna_Guitar_Tabs___Lead____Kapoor_and_Sons__Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =171)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sun_Saathiya_Guitar_Tabs___Lead___ABCD_2__Any_Body_Can_Dance_2____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =172)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rehnuma_Guitar_Tabs___Lead___ROCKY_HANDSOME___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =173)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humari_Adhuri_Kahani_Guitar_Tabs___Lead___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =174)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baaton_Ko_Teri_Guitar_Tabs___Lead___All_is_Well___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =175)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Bin_Nahi_Laage_Guitar_Tabs___Lead___Ek_Paheli_Leela___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =176)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Panchhi_Nadiya_Pawan_Ke_Jhonke_Guitar_Tabs___Lead___Refugee___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =177)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Deewani_Mastani_Guitar_Tabs___Lead___Bajirao_Mastani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =178)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def List_of_Best_Bollywood_Hindi_Love_Songs___Valentine_Day_Songs___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =179)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Shreya_Ghoshal_Guitar_Tabs___Lead___Best_of_Shreya_Ghoshal___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =180)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Wafa_Ne_Bewafai_Guitar_tabs___Lead___Teraa_Suroor___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =181)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sab_Tera_Guitar_Tabs___Lead___BAAGHI___ARMAAN_MALIK__SHRADDHA_KAPOOR___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =182)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Woh_Chaand_Guitar_Tabs___Lead___TERAA_SURROOR___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =183)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ijazat_Guitar_Tabs___Lead___ONE_NIGHT_STAND___ARIJIT_SINGH___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =184)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bol_Do_Na_Zara_Guitar_Tabs___Lead___Azhar___Armaan_Malik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =185)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bekhudi_Guitar_Tabs___Lead___Teraa_Surroor___Darshan_Raval___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =186)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yeh_Fitoor_Mera_Guitar_Tabs___Lead___Fitoor___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =187)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Manwa_Behrupiya_Guitar_Tabs___Lead___Bollywood_Diaries___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =188)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atrangi_Yaari_Guitar_Tabs___Lead___Wazir___Farhan_Akhtar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =189)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Bin_Guitar_Tabs___Lead___Wazir___Sonu_Nigam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =190)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanam_Teri_Kasam_Guitar_Tabs___Lead___Ankit_Tiwari___Mohammed_Irfan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =191)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Te_Amo_Guitar_Tabs___Lead___Dum_Maro_Dum___Ash_King___Sunidhi_Chauhan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =192)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phir_Mohabbat_Karne_Chala_Guitar_Tabs___Lead___Murder_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =193)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhse_Naraaz_Nahin_Zindagi_Guitar_Tabs___Lead___Masoom___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =194)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ambarsariya_Guitar_Tabs___Lead___Fukrey___Sona_Mohapatra___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =195)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jabra_Fan_Guitar_Tabs___Lead___Fan___Nakash_Aziz___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =196)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Itni_Si_Baat_Hai_Guitar_Tabs___Lead___Azhar___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =197)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Salamat_Guitar_Tabs___Lead___SARBJIT___ARIJIT_SINGH__TULSI_KUMAR___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =198)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Maninder_Buttar___Laare_Chords_with_Strumming_Pattern___Guitar___B_Praak___Jaani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =199)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy_Capo___Vishal_Mishra___Teri_Hogaiyaan_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =200)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Unna_Nenachu_Chords_with_Strumming_Pattern___Psycho___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =201)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Armaan_Malik___Shaamein_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =202)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy_Baari_Chords_with_Strumming_Pattern___Bilaal___Momina_Mustehsan___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =203)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Yeh_Fitoor_Mera_Chords_with_Strumming_Pattern___Guitar____w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =204)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Mera_Mehboob_Chords___Stebin___Guitar___Awez_Darbar___Nagma_Mirajkar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =205)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Accurate___Ullaallaa_Chords_with_Strumming_Pattern___Guitar___Petta___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =206)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jubin_Nautiyal___Main_Janta_Hoon_Chords_with_Strumming_Pattern___Easy___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =207)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Allah_Ve_Chords_with_Strumming_Pattern___Jassie_Gill___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =208)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy__Khuda_Hafiz_Chords_with_Strumming_Pattern___Guitar___The_Body___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =209)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Hi_Yaar_Mera_Chords_with_Strumming_Pattern___Pati_Patni_Aur_Woh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =210)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bypass_Road___Easy___Tanha_Mera_Pyaar_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =211)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Good_Newwz__Maana_Dil_Chords_with_Strumming_Pattern___Guitar___B_Praak___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =212)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh__Easy_Raanjhana_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =213)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jubin_Nautiyal__Tujhe_Kitna_Chahein_Aur_Hum_Chords___Kabir_Singh__Film_Version____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =214)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ja_Chali_Ja_Guitar_Chords_with_Strumming_Pattern___Rishabh_Tiwari___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =215)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabir_Singh___Guitar__Kaise_Hua_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =216)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehla_Pyaar_Chords_with_Strumming_Pattern__Guitar____Kabir_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =217)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Article_15__Intezari_Chords_with_Strumming_Pattern___Armaan_Malik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =218)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Sajna_Ve_Chords_Lisa_Mishra___Vishal_Mishra_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =219)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tere_Bin_Kive_Chords_with_Strumming___Ramji_Gulati___Jannat_Zubair___Mr__Faisu___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =220)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Super_30___Jugraafiya_Chords_with_Strumming_Pattern__Guitar____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =221)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Article_15__Naina_Yeh_Chords_with_Strumming_Pattern__Guitar____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =222)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Tera_Ban_Jaunga_Chords_with_Strumming___Kabir_Singh__w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =223)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Malaal__Zara_Suno_Chords_with_Strumming_Pattern__Guitar____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =224)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Papon___Har_Lamhaa_Chords_with_Strumming_Pattern__Guitar____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =225)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chehre_Padhna_Jaane_Naina___Matvaare_Chords_with_Strumming___Jubin___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =226)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Shawn_Mendes__Señorita_Guitar_Chords_with_Strumming_ft__Camila_Cabello___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =227)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Darshan_Raval___Tu_Mileya_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =228)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Diyan_Gallan_Guitar_Chords_with_Strumming___Tiger_Zinda_Hai___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =229)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy__Chukar_Mere_Man_Ko_Guitar_Chords_with_Strumming___Yaarana___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =230)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kidnap__Monta_Katha_Sonena_Guitar_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =231)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy__Tujhe_Bhula_Diya_Guitar_Chords_with_Strumming__w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =232)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mitti_Di_Khushboo_Guitar_Chords_with_Strum__w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =233)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy___Guitar__Nanhi_Pari_Chords_by_Sonu_Nigam__Asifa____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =234)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ankit_Tiwari_Guitar__Yeh_Tere_Do_Naina_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =235)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabir_Singh__Tujhe_Kitna_Chahne_Lage_Chords_with_Strumming__w_wo_Guitar_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =236)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy__Tum_Ho_Guitar_Chords_with_Strumming__w_wo_Capo____Rockstar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =237)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def _Easy__Kabir_Singh__Mere_Sohneya_Guitar_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =238)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kidnap___Guitar__Ektu_Jayga_Dena_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =239)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh__Bandeya_Guitar_Chords_with_Strumming___Dil_Junglee___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =240)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def _Easy__Bajrangi_Bhaijaan__Tu_Jo_Mila_Guitar_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =241)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humne_Rait_Pe_Chords_with_Strum___Guitar___Neha_Kakkar___Tony_Kakkar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =242)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zindagi_Di_Paudi_Guitar_Chords_with_Strumming___Millind_Gaba___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =243)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Royee_Jande_Naina_Guitar_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =244)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabira_Guitar_Chords_from_Yeh_Jawaani_Hai_Deewani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =245)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Maa_Guitar_Chords_by_Amitabh_Bachchan___Yajat___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =246)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Student_of_the_Year_2__Fakira_Guitar_Chords_with_Capo_by_Sanam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =247)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def RAETH__Bhula_Do_Bhula_Do_Guitar_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =248)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yaariyaan___Meri_Maa_Guitar_Chords_with_Strum__Two_Versions_Easy____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =249)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ami_Tomake_Bhalobashi_Guitar_Chords___KIDNAP___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =250)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chal_Para_Chords_by_Strings_Band__Guitar_Piano_Ukulele____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =251)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabir_Singh_Guitar__Bekhayali_Chords_with_Strumming__Updated____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =252)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Anxiety_Chords_by_Selena_Gomez___Julia_Michaels___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =253)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ankit_Tiwari___Guitar__Ishq_Kare_Barbadiyaan_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =254)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Indias_Most_Wanted___Guitar__Akela_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =255)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Royi_Jaye_Chords_with_Strumming___Guitar___De_De_Pyar_De___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =256)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaradhana_Ho_Aaradhana_Guitar_Chords___Worship___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =257)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Papon___Guitar__Ik_Mod_Chords_with_Strumming_Pattern___Music_Teacher___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =258)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Bhi_Nahin_Soya_Guitar_Chords___SOTY_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =259)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Music_Teacher__Sambhaal_Rakhiyaan_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =260)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Aas_Paas_Chords___Guitar_by_Yasser_Desai___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =261)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Mila_to_Haina_Chords_with_Capo___Strumming___Guitar___De_De_Pyar_De___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =262)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Se_Teri_Guitar_Chords_with_Strumming___PADMAN___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =263)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Linkin_Park_Numb_Guitar_Chords_with_Capo___Strumming__Easy____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =264)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Somebody_s_Guitar_Chords_with_Capo___Strumming___Enrique_Iglesias___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =265)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def EASY___Teri_Khaamiyan_Guitar_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =266)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def EASY__Tum_Hi_Ho_Guitar_Chords_with_Capo__Strumming___Lead___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =267)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhko_Jo_Paaya_Mere_Bina_Guitar_Chords_with_Strumming___Capo___CROOK___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =268)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Muskurane_Ki_Wajah_Guitar_Chords_with_Strumming__Easy____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =269)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def EASY__Mere_Mehboob_Qayamat_Hogi_Guitar_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =270)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mon_Aamar_Chords_by_Arko___Shesh_Theke_Shuru___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =271)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ishqe_Di_Chashni_Guitar_Chords___Strum___Bharat___Salman_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =272)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Chale_Aana_Chords_with_Capo_by_Armaan_Malik___Dede_Pyar_De___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =273)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dhvani_Bhanushali___Guitar__Vaaste_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =274)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tu_Thodi_Der_Chords_with_Capo___Strumming___Half_Girlfriend___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =275)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Music_Teacher___Guitar__Phir_Wahi_Raat_Hai_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =276)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitra__Roke_Na_Ruke_Naina_Chords_with_Capo__Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =277)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Maa_Chords_by_Ankit_Tiwari___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =278)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def KALANK___Guitar__Tabaah_Ho_Gaye_Guitar_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =279)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yasser_Desari___Guitar__Meri_Hasi_Chords_with_Strumming___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =280)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pora_Mon_Chords_with_Strumming__Easy____Ke_Tumi_Nandini___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =281)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Title_Track___Guitar__Shudhu_Tomari_Jonno_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =282)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aur_Kuch_Baki_Chords_by_Yasser_Desai___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =283)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Eka_Ekela_Mon_Guitar_Chords___Chirodini_Tumi_Je_Amar_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =284)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dosti_Guitar_Chords_with_Strumming_from_Junglee___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =285)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bastushaap___Tomake_Chuye_Dilam_Guitar_Chords___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =286)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def A_Star_Is_Born___SHALLOW_Guitar_Chords_by_Lady_Gaga___Bradley_Cooper___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =287)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Amake_Amar_Moto_Thakte_Dao_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =288)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Shaan___Guitar__Tu_Mera_Rab_Hai_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =289)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sweater___Guitar__Preme_Pora_Baron_Chords__Strumming____Bengali___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =290)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def MS_Dhoni___Guitar__Kaun_Tujhe_Chords__Easy____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =291)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def OK_Jaanu___Guitar__Enna_Sona_Chords_by_Arijit_Singh__Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =292)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def CYPHER___Guitar__Meri_Maa_Chords_by_Sonu_Nigam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =293)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def RAW___Guitar__Bulleya_Chords_by_Rabbi_Shergill___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =294)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def RAW___Guitar__Jee_Len_De_Chords_by_Mohit_Chauhan__Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =295)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def QARAN___Guitar__Haaye_Oye_Chords_ft__Ash_King__Strum____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =296)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Chala_Jata_Hoon_Guitar_Chords_by_Sanam_Puri___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =297)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh___Guitar__Kalank_Guitar_Chords_with_Strumming___Title_Track___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =298)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Junglee___Guitar__Fakeera_Ghar_Aaja_Chords___Jubin_Nautiyal___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =299)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def GUITAR__Sun_Mere_Humsafar_Chords_with_Strumming___Badrinath_Ki_Dulhania___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =300)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Half_Girlfriend___Guitar__Main_Phir_Bhi_Tumko_Chahunga_Chords__w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =301)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jubin_Nautiyal___Guitar__Chitthi_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =302)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Duniyaa_Chords_with_Strumming_Pattern___Luka_Chuppi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =303)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mere_Pyare_Prime_Minister_Chords___Title_Track___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =304)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def KK___Guitar__Tum_Na_Aaye_Chords___Badla___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =305)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def BB_Ki_Vines___Guitar__Bas_Mein_Chords___Bhuvan_Bam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =306)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh___Guitar__Ruan_Ruan_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =307)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mohit_Chauhan___Guitar__Safar_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =308)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notebook___Guitar__Laila_Chords___Dhavani_Bhanushali___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =309)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Total_Dhamaal___Guitar__Mungda_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =310)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darshan_Raval___Guitar__Kaash_Aisa_Hota_Chords__w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =311)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arko___Guitar__Shukriya_Chords___Shokhsanam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =312)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kalank___Guitar__Ghar_More_Pardesiya_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =313)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kesari__Ve_Maahi_Guitar_Chords_with_Strumming_Pattern___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =314)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kesari_Guitar__Teri_Mitti_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =315)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notebook___Guitar__Main_Taare_Chords_by_Salman_Khan__Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =316)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Luka_Chuppi___Guitar__Photo_Chords_with_Capo___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =317)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mujhse_Kaha_Naa_Gaya_Chords___Palash_Sen___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =318)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Teri_Yaad_Chords___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =319)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arko___Guitar__Shukriya_Chords_with_Capo___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =320)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Neha_Kakkar__Tera_Ghata_Chords___Guitar_Version___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =321)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tujhe_Kaise_Pata_Na_Chala_Chords__Reprise____Asees_Kaur___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =322)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tu_Meri_Zindagi_Chords_by_Keshav_Kumar___Rohan_Mehra___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =323)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atif_Aslam___Guitar__Baarishein_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =324)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Jibon_Re_Chords___Prem_Amar_2___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =325)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Ek_Galti_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =326)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Notebook___Guitar__Nai_Lagda_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =327)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dilbar_Mere_Guitar_Chords___1982___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =328)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Do_Lafzon_Ki_Hai_Guitar_Chords___The_Great_Gambler___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =329)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mohit_Chauhan___Guitar__Kyun_Dil_Mera_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =330)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dhavni_Bhanushali__Leja_Leja_Re_Guitar_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =331)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Song_Nigam__Marham_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =332)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Band___Strings__Piya_Re_Guitar_Chords___Cornetto___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =333)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Naino_Ki_To_Baat_Chords___Mera_Sanam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =334)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phir_Se___Guitar__Maine_Socha_Ke_Chura_Loon_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =335)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Band___Strings__Mil_Gaya_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =336)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jass_Gujral__Aa_bhi_Ja_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =337)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Teri_Galliyan_Chords__Unplugged_Acoustic____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =338)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Armaan_Malik___Zikr_Chords_with_Intro_Tabs___Guitar__Amavas____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =339)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darshan_Raval__Bhula_Diya_Chords___Lyrics___Guitar__With_Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =340)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Amavas___Guitar__Dhadkan_Chords_by_Jubin_Nautiyal___Palak_Muchhal___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =341)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tu_Karde_Haan_Chords___Akhil__with___without_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =342)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dhvani_Bhanushali__Main_Teri_Hoon_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =343)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tum_Mere_Ho_Chords___Vivek_Singh__Pehchaan_Music____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =344)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tum_Aisi_Kyun_Ho_Chords___Hum_Chaar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =345)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Barf_Si_Tu_Pighal_Ja_Chords___Armaan_Malik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =346)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darshan_Raval__Ek_Ladki_Ko_Dekha_To_Aisa_Laga_Guitar_Chords__Reprise____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =347)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Bheege_Bheege_Chords___Ankit_Tiwari__Sunidhi_Chauhan__Amavas____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =348)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Why_Cheat_India___Guitar__Tu_Kitna_Kaamyaab_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =349)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hum_Chaar___Guitar__Manmeet_Mere_Chords___Mohit_Chauhan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =350)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Khwaaish_Chords___Sajan_Patel___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =351)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Chehre_Chords___Harish_Verma__Punjabi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =352)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Kaise_Bhuloon_Chords___Gurnazar_Chattha___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =353)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Bairiya_Chords___Bombairiya___Arko___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =354)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Ye_Pyaar_Nahi_To_Kya_Hai_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =355)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tu_Na_Mera_Chords___Arjun_Kanungo___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =356)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Baarishein_Chords___Ankit_Rajput___Shivangi_Bhayana___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =357)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Fraud_Saiyaan___Guitar__Ishq_Ishq_Tera_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =358)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tanha_Hua_Chords___Zero___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =359)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Lae_Dooba_Chords___Aiyaary__w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =360)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Alvida_Alvida_Chords___Little_Boy___Sonu_Nigam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =361)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Toke_Chara_Chords___Jubin_Nautiyal___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =362)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Ann_Bann_Chords___Zero___Kunal_Ganjawala___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =363)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Jind_Mahi_Chords___Diljit_Dosanjh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =364)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Dil_Mein_Ho_Tum_Chords_by_Armaan_Malik___Why_Cheat_India___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =365)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Simmba__New_Tere_Bin_Guitar_Chords___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =366)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mahi_Aaja_Chords___Asim_Azhar_ft__Momina_Mustehsan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =367)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Behe_Chala_Chords___Yaseer_Desai__Shashwat_Sachdev___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =368)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Billian_Billian_Chords___Guri___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =369)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Why_Cheat_India__Phir_Mulaaqat_Chords___Guitar___Jubin_Nautiyal___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =370)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Fikar_Chords___Rahat_Fateh_Ali_Khan___Neha_Kakkar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =371)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Yasser_Desai___Tum_Chale_Gaye_Chords___Marudhar_Express___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =372)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Jo_Tu_Na_Mila_Chords___Asim_Azhar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =373)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Sakhiyaan_Chords___Maninder_Buttar___Babbu___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =374)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Teen_Cup_Chaa_Chords___Title_Track___Subho_Pramanik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =375)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Jaan_Nisaar_Chords__w_wo_Capo___Strumming____Kedarnath___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =376)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Soham_Naik___Tum_Aaoge_Chords__w_wo_Capo___Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =377)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mera_Pyar_Tera_Pyar_Chords__w_wo_Capo___Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =378)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tere_Te_Chords___Guru_Randhawa___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =379)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tu_Hi_Re_Chords___Armaan_Malik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =380)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Pinjra_Chords___Gurnazar__w_wo_Capo___Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =381)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mamla_Dil_Da_Chords___Tonny_Kakkar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =382)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bhaagte_Raho___Guitar__Gum_Hoon_Chords___Yasser_Desai___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =383)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Manush_Ekhono_Manusher_Pashe_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =384)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mujhe_Kaise_Pata_Na_Chala_Chords___Papon___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =385)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sweetheart_Guitar_Chords___Kedarnath___Dev_Negi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =386)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tere_Jisam_Chords_with_Strumming_Pattern___Altaaf_Sayyed___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =387)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Naina_Chords_by_Ankit_Tiwari___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =388)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Nazm_Nazm_Chords__Two_versions____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =389)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Meray_Saathiya_Chords___Roxen___Mustafa_Zahid___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =390)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tera_Yaar_Hoon_Main_Chords___Arijit_Singh__w_wo_Capo____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =391)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tu_Kareeb_Aaya_Chords___Rishabh_Srivastava___Aakanksha_Sharma___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =392)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Akhia_Di_Bhatkan_Chords___Sharry_Mann___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =393)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Sunn_Le_Zara_Chords___Arnab_Dutta___1921___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =394)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Allah_Duhai_Hai_Chords___Zayn___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =395)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Qaafirana_Chords_with_Strumming___Arijit_Singh___Kedarnath___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =396)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Sapna_Chords_with_Strumming_Pattern___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =397)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mere_Naam_Tu_Chords_with_Strumming_Pattern___Zero___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =398)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Aawargi_Chords_with_Strumming_Pattern___Jubin_Nautiyal___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =399)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Mein_Adhura_Lafz_Chords_with_Strumming_Pattern___Baazaar___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =400)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Dil_Zaffran_Chords_with_Strumming_Pattern___Rahat_Fateh_Ali_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =401)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Pagal_Chords_by_Diljit_Dosanjh__Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =402)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Zindagi_Mil_Jayegi_Chords___Tony___Neha_Kakkar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =403)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Teri_Judai_Mein_Chords_by_Hukam_Ali___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =404)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Baaki_Hai_Chords_with_Strumming_Pattern___Sonu_Nigam___5_Weddings___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =405)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Siren_Chords_by_The_Chainsmokers___Aazar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =406)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__If_I_Say_Chords_by_Mumford___Sons___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =407)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Got_My_Name_Changed_Back_Chords___Pisot_Annies___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =408)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Namo_Namo_Chords___Kedarnath___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =409)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Baarish_Chords_by_Neha_Kakkar___Bilal_Saeed___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =410)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Dil_Mastiyaan_Chords___Ash_King___Payal_Dev___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =411)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Kya_Baat_Ay_Chords_with_Strumming_Pattern___Hardy_Sandhu___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =412)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bhaiji__Do_Naina_Chords_with_Strumming_Pattern___Yasser_Desai_Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =413)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Jaane_Ye_Kyun_Kiya_Chords_with_Strumming_Pattern___Farhan_Akhtar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =414)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Nain_Na_Jodi_Chords_with_Strumming_Pattern___Ayushmann_Khurrana___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =415)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh__Dooba_Dooba_Chords_with_Strumming_Pattern___Guitar__Helicopter_Eela____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =416)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def KK__Pehle_Ke_Jaisa_Chords_with_Strumming_Pattern___Jalebi_Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =417)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Iktara_Chords_with_Strumming_Pattern___Wake_Up_Sid___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =418)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Dooba_Dooba_Chords_by_Sanam_Puri___Silk_Route__Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =419)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Chhod_Diya_Chords_with_Strumming_Pattern___Baazaar___Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =420)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Fakira_Chords_by_Gurnam_Bhullar___Qismat___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =421)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Soch_Na_Sake_Guitar_Chords_with_Strumming_Pattern___Airlift_Arijit_Singh___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =422)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atif__Tere_Liye_Chords_with_Strumming_Pattern___Guitar___Namaste_England___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =423)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh__Pal_Chords_with_Strumming_Pattern__Capo_Non_Capo____Guitar___Jalebi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =424)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh__Har_Har_Gange_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =425)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Tum_Se_Chords_with_Strumming_Pattern__Capo____Jubin_Nautiyal_Jalebi___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =426)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darshan_Raval__Do_Din_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =427)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar__Naina_Da_Kya_Kasoor_Chords_with_Strumming_Pattern___Andhadhun___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =428)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aap_Se_Milkar_Chords_with_Strumming_Pattern_Ayushmann_Khurrana___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =429)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Le_Ja_Tu_Kahin_Chords_with_Strumming_Pattern___Arijit_Singh_Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =430)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aye_Zindagi_Chords_with_Strumming_Pattern___Sonu_Nigam_Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =431)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit__Woh_Ladki_Chords_with_Strumming_Pattern___Andhadhun_Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =432)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Doorie_Chords_with_Strumming_Pattern___Benjamin_Rohan_Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =433)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mitron__Door_Na_Ja_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =434)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atif_Aslam__Tum_Chords_with_Strumming_Pattern___Laila_Majnu_Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =435)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jubin_Nautiyal___Sawarne_Lage_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =436)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def F_For_Fyaar_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =437)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Easy_Neele_Neele_Ambar_Par_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =438)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh___Aahista_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =439)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Nazar_Na_Lag_Jaaye_Chords_with_Strumming_Pattern___Guitar___Ash_King___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =440)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Promises_Chords_with_Strumming_Pattern___Guitar___Sam_Smith__Calvin_Harris___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =441)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sochta_Hoon___Dekhte_Dekhte_Chords___Guitar__with_Capo___without_Capo____Atif_Aslam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =442)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atif_Aslam___Chalte_Chalte_Chords_with_Strumming_Pattern__Easy____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =443)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanam_Puri___Bheegi_Bheegi_Raaton_Mein_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =444)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atif_Aslam_Tera_Hua_Chords_with_Strumming_Pattern___Loveratri___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =445)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Fanney_Khan___Tere_Jaisa_Tu_Chords_With_strumming_Pattern__Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =446)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tujhse_Naraz_Nahi_Zindagi_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =447)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hamza_Malik___O_Jaana_Chords_with_Strumming_Pattern_by_Rahat_Fateh_Ali_Khan___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =448)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atif_Aslam___Jeena_Jeena_Chords_with_Strumming_Pattern___Guitar___Badlapur___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =449)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar___Easy_Happy_Birthday_Chords_with_Strumming_Pattern__Multiple_Version____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =450)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def David_Guetta___Dont_Leave_Me_Alone_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =451)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh___Andheron_Mein_Rishtey_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =452)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Satyameva_Jayate___Tere_Jaisa_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =453)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sabrina_Claudio___Messages_From_Her_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =454)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kya_Hua_Tera_Wada_Chords_with_Strumming_Pattern___Guitar___Old_Song___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =455)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def 3_Idiots___Give_Me_Some_Sunshine_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =456)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chura_Liya_Hai_Tumne_Jo_Dil_Ko_Chords_with_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =457)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Samne_Wali_Khidki_Mein_Chords_with_Strumming_Pattern___Guitar___Old_Song___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =458)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gold___Naino_Ne_Baandhi_Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =459)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darshan_Raval___Baarish_Lete_Aana_Piano_Notes___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =460)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Naino_Ne_Baandhi_Chords___Guitar___Mouni_Roy___Akshay_Kumar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =461)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_baar_Dhadak_Chords_With_Capo_and_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =462)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sunidhi_Chauhans_Mohabbat_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =463)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_Baar_Piano_Notes___Dhadak___Jhanvi_Kapoor___Ishaan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =464)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arijit_Singh___Tera_Fitoor_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =465)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dhadak___Pehli_Baar_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =466)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atif_Aslam___Paniyo_Sa_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =467)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Fanney_Khan___Halka_Halka_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =468)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Karwaan___Saansein_Chords_With_Strumming_Pattern___Guitar___Prateek_Khulad___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =469)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chori_Chori_Jab_Nazrein_Mili_Chords_With_Strumming_Pattern_Guitar___Namita___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =470)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darshan_Raval___Baarish_Lete_Aana_Chords_With_Strumming_Pattern___With_Without_Capo___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =471)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Asees_Zaroorat_Chords_With_Strumming_Pattern___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =472)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Janhvi_Kapoor___Dhadak_Title_Track_Chords___Guitar__First_Song____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =473)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def SANJU___Ruby_Ruby_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =474)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kyun_Na_Mere_Chords___Guitar___Rishabh_Srivastava___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =475)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kanth_Kaler___Silsila_Chords___Guitar__Punjabi_Song____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =476)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Param_Singh___Jhanjar_Chords___Guitar___Punjabi_Song___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =477)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Geeta_Zaildar___Jeen_Nu_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =478)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ahida_Chords___Guitar___Shyamoli_Singh__Ravi_Singhal___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =479)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kuch_Iss_Tarah_Chords_With_Strumming_Pattern___Guitar_1921___Zareen_Khan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =480)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ayushmann_Khurrana___Chan_Kitthan_Chords_With_Strumming___Guitar____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =481)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Akhil___Rang_Gora_Chords_With_Strumming_Pattern___Guitar__Punjabi____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =482)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Satyameva_Jayate___Dilbar_Chords___Guitar___Neha_Kakkar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =483)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baaghi_2___O_Saathi_Chords_Without_Capo__Guitar____Atif_Aslam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =484)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Papa_Kehte_Hain_Chords_With_Strumming___Qayamat_Se_Qayamat_Tak___Udit_Narayan___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =485)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bhuvan_Bam___Safar_Guitar_Chords_With_Strumming_Pattern__BB_Ki_Vines____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =486)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guri___Jaan_Guitar_Chords___ALBUM_26___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =487)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kar_Har_Maidaan_Fateh_Chords___SANJU__With_Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =488)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Papon___Pakhi_Pakhi_Guitar_Chords_With_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =489)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Baaghi_2___O_Saathi_Chords_With_Capo__Guitar____Atif_Aslam___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =490)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gulabi_Aankhen_Chords_with_Guitar_Strumming_Pattern___Atif_Aslam_R_D_Burman___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =491)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sona_Mohapatra___Anhad_Naad_Guitar_Chords_With_Strumming_Pattern___Lal_Pari_Mastani___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =492)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sonu_Nigam___Chaahaton_Ke_Saaye_Mein_Guitar_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =493)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mere_Sapno_Ki_Rani_Guitar_Chords___Kishore_Kumar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =494)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Arjun_Kanungo__Momina_Mustehsan___Aaya_Na_Tu_Chords___Guitar___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =495)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Dua_Hai_Guitar_Chords___Tabs__Darshan_Raval___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =496)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Guitar_Chords_of_Darasal___Atif_Aslam___Raabta__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =497)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rahul_Vaidya___Keh_Do_Na_Guitar_Chords_with_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =498)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def De_De_Jagah_Guitar_Chords_with_Strumming_Pattern___Parmanu___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =499)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gal_Sun_Jayein_Guitar_Chords___Akhil_Sachdeva__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =500)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pyar_Nai_Karna_Aya_Guitar_Chords___Karan_Juneja___Punjabi__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =501)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sare_Karo_Dab_Guitar_Chords___Sonu_Kakkar__Raftaar__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =502)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aa_Jao_Na_Guitar_Chords___Arijit_Singh___Veere_Di_Wedding__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =503)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jitni_Dafa_Guitar_Chords_From_Parmanu_With_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =504)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Meri_Aashiqui_Guitar_Chords___Balraj_With_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =505)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ghar_Se_Nikalte_Hi_Guitar_Chords___Armaan_Malik___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =506)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def SANJU___Main_Badhiya_Tu_Bhi_Badhiya_Guitar_Chords_With_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =507)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Harsohena___Tere_Bin_Guitar_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =508)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Andra___Sudamericana_Guitar_Chords_With_Strumming_Pattern___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =509)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ae_Watan_Guitar_Chords___Arijit_Singh___Raazi__With_Strumming____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =510)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Selfish_Guitar_Chords___Atif_Aslam___Race_3__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =511)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Heeriye_Guitar_Chords_with_Intro_Tabs___Race_3___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =512)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Ghata_Guitar_Chords___Gajendra_Verma__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =513)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humnava_Mere_Guitar_Chords___Jubin_Nautiyal__With_Strumming_Pattern____Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =514)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Diyan_Gallan_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =515)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Se_Teri_Guitar_Chords___Strumming_Pattern___Padman(request):
	text = Sargams.objects.filter(id__iexact =516)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanu_Ek_Pal_Chain_Guitar_Chords___Strumming_Pattern___Raid(request):
	text = Sargams.objects.filter(id__iexact =517)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lae_Dooba_Guitar_Chords___Strumming_Pattern___Aiyaary(request):
	text = Sargams.objects.filter(id__iexact =518)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def O_Saathi_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =519)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Yaar_Hoon_Main_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =520)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gazab_Ka_Hai_Din_Guitar_Chords___Strumming_Pattern___Dil_Juunglee(request):
	text = Sargams.objects.filter(id__iexact =521)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lo_Safar_Guitar_Chords___Strumming_Pattern___Baaghi_2(request):
	text = Sargams.objects.filter(id__iexact =522)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Meri_Khamoshi_Hai_Guitar_Chords___Strumming_Pattern___Pari(request):
	text = Sargams.objects.filter(id__iexact =523)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Theher_Ja_Guitar_Chords___Strumming_Pattern___October(request):
	text = Sargams.objects.filter(id__iexact =524)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Boond_Boond_Guitar_Chords___Strumming_Pattern___Hate_Story_4(request):
	text = Sargams.objects.filter(id__iexact =525)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ye_Ishq_Hai_Guitar_Chords___Strumming_Pattern___Rangoon___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =526)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Dil_Mein_Guitar_Chords___Strumming_Pattern___Armaan_Malik(request):
	text = Sargams.objects.filter(id__iexact =527)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def 25_Most_Romantic_Bollywood_Songs_Guitar_Chords_For_Valentine_Week(request):
	text = Sargams.objects.filter(id__iexact =528)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kho_Diya_Guitar_Chords___Strumming_Pattern___Bhoomi(request):
	text = Sargams.objects.filter(id__iexact =529)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Bina_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =530)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humsafar_Guitar_Chords___Strumming_Pattern___badrinath_ki_dulhania(request):
	text = Sargams.objects.filter(id__iexact =531)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Meet_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =532)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hawayein_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =533)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ghar_Guitar_Chords___Strumming_Pattern___Jab_Harry_Met_Sejal(request):
	text = Sargams.objects.filter(id__iexact =534)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Mere_Darmiyaan_Guitar_Chords___Strumming_Pattern___Chef(request):
	text = Sargams.objects.filter(id__iexact =535)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jaane_de_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =536)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Love_You_Zindagi_Guitar_Chords___Strumming_Pattern___Dear_Zindagi(request):
	text = Sargams.objects.filter(id__iexact =537)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Channa_Mereya_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =538)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def The_Humma_Song_Guitar_Chords___Strumming_Pattern___OK_Jaanu(request):
	text = Sargams.objects.filter(id__iexact =539)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Hi_Hai_Guitar_Chords___Strumming_Pattern___Dear_Zindagi(request):
	text = Sargams.objects.filter(id__iexact =540)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Nashe_Si_Chadh_Gayi_Guitar_Chords___Strumming_Pattern___Befikre(request):
	text = Sargams.objects.filter(id__iexact =541)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Enna_Sona_Guitar_Chords___Strumming_Pattern___OK_Jaanu(request):
	text = Sargams.objects.filter(id__iexact =542)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zaalima_Guitar_Chords___Strumming_Pattern___Raees(request):
	text = Sargams.objects.filter(id__iexact =543)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_Dafa_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =544)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bawara_Mann_Guitar_Chords___Strumming_Pattern___Jolly_LLB_2(request):
	text = Sargams.objects.filter(id__iexact =545)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Orrey_Mon_Guitar_Chords___Strumming_Pattern___Ayushmann_Khurrana(request):
	text = Sargams.objects.filter(id__iexact =546)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bulleya_Guitar_Chords___Strumming_Pattern___Ae_Dil_Hai_Mushkil(request):
	text = Sargams.objects.filter(id__iexact =547)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kaabil_Hoon_Guitar_Chords___Strumming_Pattern___Kaabil(request):
	text = Sargams.objects.filter(id__iexact =548)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dariya_Guitar_Chords___Strumming_Pattern___Baar_Baar_Dekho(request):
	text = Sargams.objects.filter(id__iexact =549)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dhal_Jaun_Main_Guitar_Chords___Strumming_Pattern___Rustom(request):
	text = Sargams.objects.filter(id__iexact =550)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darkhaast_Guitar_Chords___Strumming_Pattern___Shivaay(request):
	text = Sargams.objects.filter(id__iexact =551)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Toota_Jo_Kabhi_Tara_Guitar_Chords___Strumming___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =552)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kho_Gaye_Hum_Kahan_Guitar_Chords___Strumming___Baar_Baar_Dekho(request):
	text = Sargams.objects.filter(id__iexact =553)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Besabriyaan_Guitar_chords___Strumming_Pattern___M_S_Dhoni(request):
	text = Sargams.objects.filter(id__iexact =554)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ae_Dil_Hai_Mushkil_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =555)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sau_Aasmaan_Guitar_Chords___Strumming_Pattern___Baar_Baar_Dekho(request):
	text = Sargams.objects.filter(id__iexact =556)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Raaz_Aankhein_Teri_Guitar_Chords___Strumming_Pattern___Raaz_Reboot(request):
	text = Sargams.objects.filter(id__iexact =557)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yaad_Hai_Na_Guitar_Chords___Strumming_Pattern___Raaz_Reboot(request):
	text = Sargams.objects.filter(id__iexact =558)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phir_Kabhi_Guitar_Chords___Strumming_Pattern___M_S_Dhoni(request):
	text = Sargams.objects.filter(id__iexact =559)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jaago_Guitar_chords___Strumming_Pattern___Rock_on_2(request):
	text = Sargams.objects.filter(id__iexact =560)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aadat_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =561)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zara_Si_Dosti_Guitar_Chords___Strumming_Pattern___Happy_Bhag_Jayegi(request):
	text = Sargams.objects.filter(id__iexact =562)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kuch_Toh_Hai_Guitar_Chords___Strumming_Pattern___Do_Lafzon_Ki_Kahani(request):
	text = Sargams.objects.filter(id__iexact =563)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mujhko_Barsaat_Bana_Lo_Guitar_Chords___Strumming_Pattern___Junooniyat(request):
	text = Sargams.objects.filter(id__iexact =564)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pani_Da_Rang_Guitar_Chords___Strumming_Pattern___Vicky_Donor(request):
	text = Sargams.objects.filter(id__iexact =565)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Alvida_Guitar_Chords___Strumming_Pattern___Traffic(request):
	text = Sargams.objects.filter(id__iexact =566)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ishqe_Di_Lat_Guitar_Chords___Strumming_Pattern___Junooniyat(request):
	text = Sargams.objects.filter(id__iexact =567)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ikk_Kudi_Guitar_Chords___Strumming_Pattern___Udta_Punjab(request):
	text = Sargams.objects.filter(id__iexact =568)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mile_Ho_Tum_Humko_Guitar_Chords___Strumming_Pattern___Fever(request):
	text = Sargams.objects.filter(id__iexact =569)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Yaad_Guitar_Chords___Strumming_Pattern___Fever(request):
	text = Sargams.objects.filter(id__iexact =570)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Sang_Yaara_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =571)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dekha_Hazaro_Dafaa_Guitar_Chords___Strumming_Pattern___Rustom(request):
	text = Sargams.objects.filter(id__iexact =572)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Le_Chala_Guitar_Chords___Strumming_Pattern___One_Night_Stand(request):
	text = Sargams.objects.filter(id__iexact =573)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ijazat_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =574)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Awargi_Guitar_Chords___Strumming_Pattern___Love_Games(request):
	text = Sargams.objects.filter(id__iexact =575)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Itni_Si_Baat_Hai_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =576)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bol_Do_Na_Zara_Guitar_Chords___Strumming_Pattern___Azhar(request):
	text = Sargams.objects.filter(id__iexact =577)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Girl_I_Need_You_Guitar_Chords___Strumming_Pattern___Baaghi(request):
	text = Sargams.objects.filter(id__iexact =578)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aafreen_Guitar_Chords___Strumming_Pattern___1920_London(request):
	text = Sargams.objects.filter(id__iexact =579)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rootha_Kyun_Guitar_Chords___Strumming_Pattern___1920_London(request):
	text = Sargams.objects.filter(id__iexact =580)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_Nazar_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =581)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Salamat_Guitar_Chords___Strumming_Pattern___Sarbjit(request):
	text = Sargams.objects.filter(id__iexact =582)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehla_Nasha_Guitar_Chords___Strumming_Pattern___Amir_Khan(request):
	text = Sargams.objects.filter(id__iexact =583)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zara_Sa_Guitar_Chords___Strumming_Pattern___Jannat(request):
	text = Sargams.objects.filter(id__iexact =584)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Woh_Chaand_Guitar_Chords___Strumming___Teraa_Surroor(request):
	text = Sargams.objects.filter(id__iexact =585)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tera_Chehra_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =586)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Manwa_Behrupiya_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =587)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bolna_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =588)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bekhudi_Guitar_Chords___Strumming_Pattern___Teraa_Surroor(request):
	text = Sargams.objects.filter(id__iexact =589)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Mere_Paas_Guitar_Chords___Strumming_Pattern___Wazir(request):
	text = Sargams.objects.filter(id__iexact =590)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gazab_Ka_Hai_Ye_Din_Guitar_Chords___Strumming_Pattern___Sanam_Re(request):
	text = Sargams.objects.filter(id__iexact =591)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Rehnuma_Guitar_Chords___Strumming_Pattern___Rocky_Handsome(request):
	text = Sargams.objects.filter(id__iexact =592)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ji_Huzoori_Guitar_Chords___Strumming_pattern___Ki_And_Ka(request):
	text = Sargams.objects.filter(id__iexact =593)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sab_Tera_Guitar_Chords___Strumming_Pattern___Baaghi(request):
	text = Sargams.objects.filter(id__iexact =594)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Wafa_Ne_Bewafai_Guitar_Chords___Strumming_Pattern___Teraa_Surroor(request):
	text = Sargams.objects.filter(id__iexact =595)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Agar_Tu_Hota_Guitar_Chords___Strumming_Pattern___Baaghi(request):
	text = Sargams.objects.filter(id__iexact =596)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Soch_Na_Sake_Guitar_Chords___Strumming_Pattern___Airlift(request):
	text = Sargams.objects.filter(id__iexact =597)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumhe_Apna_Banane_ka_Junoon_Guitar_Chords___Strumming_Pattern___Hate_Story_3(request):
	text = Sargams.objects.filter(id__iexact =598)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gerua_Guitar_Chords___Strumming_Pattern___Dilwale(request):
	text = Sargams.objects.filter(id__iexact =599)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Safarnama_Guitar_Chords___Strumming_Pattern___Tamasha(request):
	text = Sargams.objects.filter(id__iexact =600)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Mar_Jaayen_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =601)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Janam_Janam_Guitar_Chords___Strumming_Pattern___Dilwale(request):
	text = Sargams.objects.filter(id__iexact =602)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sathia_Guitar_Chords___Strumming_Pattern___Ankit_Tiwari(request):
	text = Sargams.objects.filter(id__iexact =603)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yeh_Fitoor_Mera_Guitar_Chords___Strumming_Pattern___Fitoor(request):
	text = Sargams.objects.filter(id__iexact =604)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sanam_Re_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =605)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Atrangi_Yaari_Guitar_Chords___Strumming_Pattern___Wazir(request):
	text = Sargams.objects.filter(id__iexact =606)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bandeya_Guitar_Chords___Strumming_Pattern___Jazbaa(request):
	text = Sargams.objects.filter(id__iexact =607)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Nazdeekiyan_Guitar_Chords___Strumming_Pattern___Shaandaar(request):
	text = Sargams.objects.filter(id__iexact =608)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Woh_Dekhne_Me_Guitar_Chords___Strumming_Pattern___Ali_Zafar(request):
	text = Sargams.objects.filter(id__iexact =609)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lukka_Chuppi_Guitar_Chords___Strumming_Pattern___Rang_De_Basanti(request):
	text = Sargams.objects.filter(id__iexact =610)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zara_Zara_Guitar_Chords___Strumming_Pattern___RHTDM(request):
	text = Sargams.objects.filter(id__iexact =611)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Moora_Guitar_Chords___Strumming_Pattern___Gangs_Of_Wasseypur_2(request):
	text = Sargams.objects.filter(id__iexact =612)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Awari_Guitar_Chords___Strumming_Pattern___Ek_Villain(request):
	text = Sargams.objects.filter(id__iexact =613)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Iss_Qadar_Pyar_Hai_Guitar_Chords___Strumming_Pattern___Bhaag_Johnny(request):
	text = Sargams.objects.filter(id__iexact =614)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Be_Intehaan_Guitar_Chords___Strumming_Pattern___Race_2(request):
	text = Sargams.objects.filter(id__iexact =615)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Khoya_Khoya_Guitar_Chords___Strumming_Pattern___Hero(request):
	text = Sargams.objects.filter(id__iexact =616)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sau_Aasoon_Guitar_Chords___Strumming_Pattern___Katti_Batti(request):
	text = Sargams.objects.filter(id__iexact =617)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def _Rock__Khwaishein_Guitar_Chords___Strumming_Pattern___Calender_Girls(request):
	text = Sargams.objects.filter(id__iexact =618)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Khwaishein_Guitar_Chords___Strumming_Pattern___Calender_Girls(request):
	text = Sargams.objects.filter(id__iexact =619)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Woh_Lamhe_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =620)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Roobaroo_Guitar_Chords___Strumming_Pattern___Rang_De_Basanti(request):
	text = Sargams.objects.filter(id__iexact =621)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hona_Tha_Pyar_Guitar_chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =622)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bhaag_Dk_Bose_Guitar_Chords___Strumming_Pattern___Delhi_Belly(request):
	text = Sargams.objects.filter(id__iexact =623)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chal_Chale_Apne_Ghar_Guitar_Chords___Strumming_Pattern___Woh_Lamhe(request):
	text = Sargams.objects.filter(id__iexact =624)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hai_Koi_Guitar_Chords___Strumming_Pattern___Gajendra_Verma(request):
	text = Sargams.objects.filter(id__iexact =625)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phoolon_Ka_Taaro_Ka_Guitar_Chords___Strumming_Pattern___Raksha_Bandhan(request):
	text = Sargams.objects.filter(id__iexact =626)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Yaaron_Dosti_Guitar_Chords___Strumming_Pattern___Kk(request):
	text = Sargams.objects.filter(id__iexact =627)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Jo_Mila_Guitar_Chords___Strumming_Pattern___Bajrangi_Bhaijaan(request):
	text = Sargams.objects.filter(id__iexact =628)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zehnaseeb_Guitar_Chords___Strumming_Pattern___Hasee_Toh_Phasee(request):
	text = Sargams.objects.filter(id__iexact =629)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Na_Jaane_Aas_Pass_Hai_Khuda_Guitar_Chords___Strumming_Pattern(request):
	text = Sargams.objects.filter(id__iexact =630)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Hoon_Hero_Tera_Guitar_Chords___Strumming_Pattern___Hero(request):
	text = Sargams.objects.filter(id__iexact =631)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ove_Janiya_Guitar_Chords___Strumming_Pattern___Katti_Batti(request):
	text = Sargams.objects.filter(id__iexact =632)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Banjarey_Guitar_Chords___Strumming_Pattern_By_Honey_Singh___Fugly(request):
	text = Sargams.objects.filter(id__iexact =633)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Galliyan_Guitar_Chords___Strumming_Pattern___Ek_Villian(request):
	text = Sargams.objects.filter(id__iexact =634)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Hi_Ho_Guitar_Chords___Strumming_Pattern_By_Arijit_Singh___Aashiqui_2(request):
	text = Sargams.objects.filter(id__iexact =635)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ilahi_Guitar_Chords___Strumming_Pattern_by_Arijit_Singh___Yeh_Jawaani_Hai_Deewani(request):
	text = Sargams.objects.filter(id__iexact =636)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_Baar_Guitar_Chords___Strumming_Pattern___Dil_Dhadakne_Do(request):
	text = Sargams.objects.filter(id__iexact =637)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ambarsariya_Guitar_Chords___Strumming_Pattern___Fukrey(request):
	text = Sargams.objects.filter(id__iexact =638)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Ho_Toh_Guitar_Chords___Strumming_Pattern___Rock_On(request):
	text = Sargams.objects.filter(id__iexact =639)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pichle_Saat_Dino_Me_Guitar_Chords___Strumming_Pattern___Rock_On(request):
	text = Sargams.objects.filter(id__iexact =640)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Saware_Guitar_Chords___Strumming_Pattern_By_Arijit_Singh___Phantom(request):
	text = Sargams.objects.filter(id__iexact =641)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Give_Me_Some_Sunshine_Guitar_Chords___Strumming_Pattern__3_Idiots(request):
	text = Sargams.objects.filter(id__iexact =642)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kabira_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =643)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tu_Chahiye_Guitar_Chords___Strumming_Pattern___Bajrangi_Bhaijaan(request):
	text = Sargams.objects.filter(id__iexact =644)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jhoom_Guitar_Chords__Strumming_Pattern___Ali_Zafar(request):
	text = Sargams.objects.filter(id__iexact =645)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hamari_Adhuri_Kahani_Guitar_Chords___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =646)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hasi_Ban_Gaye_Guitar_Chords___Hamari_Adhuri_Kahani(request):
	text = Sargams.objects.filter(id__iexact =647)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Gulabi_Aankhen_Atif_Aslam_Guitar_Chords___Strumming_Pattern(request):
	text = Sargams.objects.filter(id__iexact =648)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jeena_Jeena_Guitar_Chords___Atif_Aslam_Badlapur(request):
	text = Sargams.objects.filter(id__iexact =649)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kuch_Bhi_Karlo_Guitar_Chords___Swastik_the_Band(request):
	text = Sargams.objects.filter(id__iexact =650)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Chal_Chale_Apne_Ghar_Guitar_Chords___Strumming_Pattern___Woh_Lamhe(request):
	text = Sargams.objects.filter(id__iexact =651)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dekha_Hazaro_Dafaa_Guitar_Chords___Strumming_Pattern___Rustom(request):
	text = Sargams.objects.filter(id__iexact =652)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bolna_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =653)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Soch_Na_Sake_Guitar_Chords___Strumming_Pattern___Airlift(request):
	text = Sargams.objects.filter(id__iexact =654)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Rahoon_Ya_Na_Rahoon_Guitar_Chords___Emraan_Hashmi(request):
	text = Sargams.objects.filter(id__iexact =655)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tumhe_Apna_Banane_ka_Junoon_Guitar_Chords___Strumming_Pattern___Hate_Story_3(request):
	text = Sargams.objects.filter(id__iexact =656)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zara_Sa_Guitar_Chords___Strumming_Pattern___Jannat(request):
	text = Sargams.objects.filter(id__iexact =657)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Iss_Qadar_Pyar_Hai_Guitar_Chords___Strumming_Pattern___Bhaag_Johnny(request):
	text = Sargams.objects.filter(id__iexact =658)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Main_Hoon_Hero_Tera_Guitar_Chords___Strumming_Pattern___Hero(request):
	text = Sargams.objects.filter(id__iexact =659)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tere_Sang_Yaara_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =660)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Tum_Hi_Ho_Guitar_Chords___Strumming_Pattern_By_Arijit_Singh___Aashiqui_2(request):
	text = Sargams.objects.filter(id__iexact =661)
	lists = Sargams.objects.filter(song_names__icontains='lo')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jeena_Jeena_Guitar_Chords___Atif_Aslam_Badlapur(request):
	text = Sargams.objects.filter(id__iexact =662)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Zehnaseeb_Guitar_Chords___Strumming_Pattern___Hasee_Toh_Phasee(request):
	text = Sargams.objects.filter(id__iexact =663)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jhoom_Guitar_Chords__Strumming_Pattern___Ali_Zafar(request):
	text = Sargams.objects.filter(id__iexact =664)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Be_Intehaan_Guitar_Chords___Strumming_Pattern___Race_2(request):
	text = Sargams.objects.filter(id__iexact =665)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Teri_Meri_Kahani_Guitar_Chords___Strumming_Pattern___BB_Ki_Vines(request):
	text = Sargams.objects.filter(id__iexact =666)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Phir_Kabhi_Guitar_Chords___Strumming_Pattern___M_S_Dhoni(request):
	text = Sargams.objects.filter(id__iexact =667)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Pehli_Nazar_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =668)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Darkhaast_Guitar_Chords___Strumming_Pattern___Shivaay(request):
	text = Sargams.objects.filter(id__iexact =669)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Kho_Diya_Guitar_Chords___Strumming_Pattern___Bhoomi(request):
	text = Sargams.objects.filter(id__iexact =670)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Meet_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =671)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Humsafar_Guitar_Chords___Strumming_Pattern___badrinath_ki_dulhania(request):
	text = Sargams.objects.filter(id__iexact =672)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Sang_Hoon_Tere_Guitar_Chords___Strumming_Pattern___Bhuvan_Bam(request):
	text = Sargams.objects.filter(id__iexact =673)
	lists = Sargams.objects.filter(song_names__icontains='n')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hawayein_Guitar_Chords___Strumming_Pattern___Arijit_Singh(request):
	text = Sargams.objects.filter(id__iexact =674)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Dil_Diyan_Gallan_Guitar_Chords___Strumming_Pattern___Atif_Aslam(request):
	text = Sargams.objects.filter(id__iexact =675)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Aaj_Se_Teri_Guitar_Chords___Strumming_Pattern___Padman(request):
	text = Sargams.objects.filter(id__iexact =676)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Vance_Joy___Riptide_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =677)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Judy_Garland___Somewhere_Over_The_Rainbow___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =678)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def John_Legend___All_Of_Me_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =679)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Lukas_Graham___7_Years_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =680)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ruth_B___Lost_Boy_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =681)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def The_Chainsmokers___Closer_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =682)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Plain_White_Ts___Hey_There_Delilah_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =683)
	lists = Sargams.objects.filter(song_names__icontains='d')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Justin_Bieber___Love_Yourself_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =684)
	lists = Sargams.objects.filter(song_names__icontains='c')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Simon_And_Garfunkel___The_Sound_Of_Silence_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =685)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Oasis___Wonderwall_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =686)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jason_Mraz___Im_Yours_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =687)
	lists = Sargams.objects.filter(song_names__icontains='s')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def James_Bay___Let_It_Go_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =688)
	lists = Sargams.objects.filter(song_names__icontains='b')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Hillsong_United___Oceans_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =689)
	lists = Sargams.objects.filter(song_names__icontains='l')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ed_Sheeran___Thinking_Out_Loud_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =690)
	lists = Sargams.objects.filter(song_names__icontains='t')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Bon_Iver___Skinny_Love_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =691)
	lists = Sargams.objects.filter(song_names__icontains='a')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Beatles___Hey_Jude_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =692)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Adele___Someone_Like_You_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =693)
	lists = Sargams.objects.filter(song_names__icontains='m')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Eagles___Hotel_California_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =694)
	lists = Sargams.objects.filter(song_names__icontains='e')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Jeff_Buckley___Hallelujah_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =695)
	lists = Sargams.objects.filter(song_names__icontains='p')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

def Ed_Sheeran___Photograph_Chords___Abhijeet(request):
	text = Sargams.objects.filter(id__iexact =696)
	lists = Sargams.objects.filter(song_names__icontains='pyar')[:10]
	context={'songs' : text,'lists':lists}
	return render(request,'music/songs.html',context)

