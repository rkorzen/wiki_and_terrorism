import numpy as np

ideology = {
'Hezbollah Al-Hejaz (suspected))': 'Islamic',
'Islamic State':'Islamic',

'Taliban':'Islamic',

'Lone wolf':'Lone wolf',

"Lashkar-e-Jhangvi (suspected)":"Islamic",

"Lashkar-e-Jhangvi":'Islamic',

'Al-Qaeda in the Islamic Maghreb (suspected)':'Islamic',

'Al-Shabaab':'Islamic',

'Al-Qaeda in the Arabian Peninsula':'Islamic',

'Anti-balaka (suspected)':'Islamic',

'Bangsamoro Islamic Freedom Fighters (suspected)':'Islamic',

'Boko Haram':'Islamic',

'Mapuche':'Mapuche',

'Islamic State (suspected)':'Islamic',

'Kurdistan Freedom Falcons[31]':'Kurds',

'Nordic Resistance Movement (suspected)':'Nazism',

'Lashkar-e-Jhangvi':'Islamic',

'Taliban (suspected)':'Islamic',

'Kangleipak Communist Party[42]':'Communism',

'Boko Haram (suspected)':'Islamic',

'Unknown':'Unknown',

'Militants':'Kashmir',

'National Liberation Army':'Communism',

'Anarchists (suspected)':'Anarchism',

'Lashkar-e-Taiba (suspected)':'Islamic',

'Salafist jihadist (suspected)':'Islamic',

'Lone Wolf':'Lone wolf',

'Abu Sayyaf (suspected)':'Islamic',

"Paraguayan People's Army (suspected)":'Communism',

'Al-Qaeda (suspected)':'Islamic',

'Tehreek-e-Taliban':'Islamic',

'Óglaigh na hÉireann (Real IRA splinter group)':"IRA",

'Fulani herdsmen':'Other',

'Militant Guerillas (suspected)':'Communism',

"Kurdistan Workers' Party":'Kurds',

"Luhansk People's Republic (suspected)":"Russian Separatists",

'Al-Mourabitoun':'Islamic',

'Islamic Movement in Israel (suspected)':'Islamic',

'Naxalites':'Communism',

'Lashkar-e-Jhangvi & Tehrik-i-Taliban Pakistan':'Islamic',

'Jabhat Fatah al-Sham (suspected)':'Islamic',

'Real Irish Republican Army (suspected)':'IRA',

'Conspiracy of Fire Nuclei':'Anarchism',

'Democratic Union Party':"Kurds",

'Islamists':'Islamic',

'Abu Sayyaf':'Islamic',

'Alexandre Bissonnette (suspected)':'anti-islamic',

'Ansar Dine (suspected)':'Islamic',

"New People's Army":'Communism',

np.nan: "Other",

'Nuer White Army (suspected)':'Other',

'Naxalites (suspected)':'Communism',

'Anarchists':'Anarchism',

'Islamic State – Sinai Province':'Islamic',

'Ukrainian anarchists':'Anarchism',

'Ansar Dine':'Islamic',

'Al-Qaeda in the Islamic Maghreb':'Islamic',

'Islamic State – Khorasan Province':'Islamic',

'Taliban or Islamic State – Khorasan Province (suspected)':'Islamic',

'Tehreek-i-Taliban':'Islamic',

'Jamaat-ul-Ahrar':'Islamic',

'Pravy Sektor':'Nationalism',

'Turkistan Islamic Party (suspected)':'Islamic',

'Islamic State – Yemen Province':'Islamic',

'Tehrik-i-Taliban Pakistan':'Islamic',

'Islamic State – Sinai Province (suspected)':'Islamic',

"New People’s Army":'Communism',

'Al-Shabaab (suspected)':'Islamic',

'National Liberation Army (suspected)':'Communism',

'United Armed Forces of Novorossiya (suspected)':"Russian Separatists",

'Opponents':"Other",

'Dissident republicans':"IRA",

'Popular Front for the Rebirth of Central African Republic':'Islamic',

'New Irish Republican Army':'IRA',

'Benghazi Shura Council (suspected)':'Islamic',

'Hizbul Mujahideen':'Islamic',

'Al-Qaeda in the Arabian Peninsula (suspected)':'Islamic',

'Tahrir al-Sham':'Islamic',

'Lone wolf (suspected)':'Lone wolf',

'Islamic State – Algeria Province':'Islamic',

'Ansar ul Islam':'Islamic',

'Jaish-e-Mohammed':'Islamic',

"Jama'at Nasr al-Islam wal Muslimin":'Islamic',

'ELN':'Communism',

'ELN and Autodefensas Gaitanistas':'Communism',

'Lashkar-e-Taiba':'Islamic',

'Communist Party of India (Maoist) (suspected)':'Communism',

"Jama'at Nasr al-Islam wal Muslimin (suspected)":'Islamic',

'Sendero Luminoso':"Communism",

'Ulster Defence Association (suspected)':"Anti-IRA",

'Tahrir al-Sham (suspected)':'Islamic',

'Jihadists':'Islamic',

'PKK':"Kurds",

'Allied Democratic Forces (suspected)':"Other",

'Jihadist':'Islamic',

'Shining Path':'Communism',

'Jalisco New Generation Cartel (suspected)':"Cartel",

"Donetsk People's Republic":"Russian Separatists",

'Khalid Masood':'Islamic',

'Jamaat-ul-Ahrar (suspected)':'Islamic',

'Kamwina Nsapu':"Other",

'White Supremecist':'Racism',

'Islamic State in Somalia':'Islamic',

'Bangsamoro Islamic Freedom Fighters':'Islamic',

'Kamwina Nsapu (suspected)':"Other",

"Donetsk People's Republic (suspected)":"Russian Separatists",

'Turkish Nationalists (suspected)':'Nationalism',

'Runda Kumpulan Kecil (suspected)':'Islamic',

'Palestinian Nationalist':'Nationalism',

'The Hasm Movement (suspected)':'Islamic',

'Imam Shamil Battalion':'Islamic',

'Tehreek-i-Taliban Pakistan':'Islamic',

'National Liberation Front of Corsica':'Nationalism',

'Tehreek-i-Taliban Pakistan (suspected)':'Islamic',

'Jaish-e-Mohammed (suspected)':'Islamic',

'Al Shabaab (suspected)':'Islamic',

'Rakhmat Akilov':'Islamic',

'Vilayat Dagestan (suspected)':'Islamic',

'Jihadist (suspected)':'Islamic',

'FARC (suspected)':'Communism',

"Sudan People's Liberation Army (suspected)":"Other",

'Mullah Dadullah Front (suspected)':'Islamic',

'Islamists (suspected)':'Islamic',

'Ahrar al-Sham (suspected)':'Islamic',

'PKK (suspected)':'Kurds',

'Khalid ibn al-Walid Army (suspected)':'Islamic',

'Kori Ali Muhammad':'Islamic',

'Neo Nazi (suspected)':'Nazism',

'Islamic State in Somalia (suspected)':'Islamic',

'CPI (suspected)':'Communism',

'Jaish ul-Adl (suspected)':'Islamic',

'ELN (suspected)':'Communism',

'EPP':'Communism',

'ELN and EPL':'Communism',

'EPL':'Communism',

'Anarcho-syndicalists (suspected)':'Anarchism',

'Runda Kumpulan Kecil':'Islamic',

'Islamic State of Iraq and the Levant in Libya (suspected)':'Islamic',

'Islamic Army in Iraq (suspected)':'Islamic',

'Séléka (suspected)':'Islamic',

'Democratic Liberation Forces of Rwanda':'Nationalism',

'Los Urabeños (suspected)':'Cartel',

'Jamaat-ul-Mujahideen':'Islamic',

'Militant Anarchist (suspected)':'Anarchism',

'Houthis':'Islamic',

'Los Urabeños':'Cartel',
'Bundu dia Kongo (suspected)':'Bundu',
'Haqqani network (suspected)':'Islamic',

'Balochistan Liberation Army':'Other',
'Balochistan Liberation Army (suspected)':'Other',

'Misrata Militants (suspected)':'Unknown',
'Barisan Revolusi Nasional (suspected)':'Nationalism',
'Tehrik-e-Taliban':'Islamic',
'Islamist':'Islamic',
'AQIM (suspected)':'Islamic',
'Jamaah Ansharut Tauhid':'Islamic',
'Islamic State]':'Islamic',
'Taliban or Islamic State':'Islamic',
'PJAK':'Unknown',
'Haqqani Network (suspected)':'Islamic',
'al-Shabaab (suspected)':'Islamic',
'Hezbollah Al-Hejaz (suspected)':'Islamic',
'Los Zetas (suspected)':'Cartel',
'Al Shabaab':'Islamic',
'Naxals':'Communism',
'Islamic State (claimed)':'Islamic',
'Mai-mai Militants (suspected)':'Other',
'Hezbollah Al-Hejaz (suspected)':'Islamic'}