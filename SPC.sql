select top(2) Towar.tw_Id, Towar.tw_Symbol, Towar.tw_Nazwa, Stan.st_Stan, Towar.tw_PodstKodKresk, Zdjecie.zd_Zdjecie 
from tw__Towar as Towar
JOIN tw_Stan as Stan on Stan.st_TowId = Towar.tw_Id
LEFT JOIN tw_ZdjecieTw as Zdjecie on Zdjecie.zd_IdTowar = Towar.tw_Id
where Stan.st_MagId = 1
and Zdjecie.zd_Glowne = 1;

select top(30) * from tw_ZdjecieTw where zd_IdTowar = 21614 ang zd_Glowne=1
;

select * from sl_Magazyn;

select top(10) * from tw_Stan where st_MagId = 1;
select * from tw_Stan where st_TowId = 11 and st_MagId = 1;

select * from kh__Kontrahent where kh_Cena = 7;

select top(1) * from tw__Towar;