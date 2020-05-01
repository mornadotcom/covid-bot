#!/usr/bin/python3

def get_district_code_from_passing(passing):
	dists = {
	"MH01" : "Mumbai",
	"MH02" : "Mumbai",
	"MH03" : "Mumbai",
	"MH04" : "Thane",
	"MH06" : "Raigad",
	"MH07" : "Sindhudurg",
	"MH08" : "Ratnagiri",
	"MH09" : "Kolhapur",
	"MH10" : "Sangli",
	"MH11" : "Satara",
	"MH12" : "Pune",
	"MH13" : "Solapur",
	"MH14" : "Pimpri",
	"MH15" : "Nashik",
	"MH16" : "Ahmednagar",
	"MH17" : "Shrirampur",
	"MH18" : "Dhule",
	"MH19" : "Jalgaon",
	"MH20" : "Aurangabad",
	"MH21" : "Jalna",
	"MH22" : "Parbhani",
	"MH23" : "Beed",
	"MH24" : "Latur",
	"MH25" : "Osmanabad",
	"MH26" : "Nanded",
	"MH27" : "Amravati",
	"MH28" : "Buldana",
	"MH29" : "Yavatmal",
	"MH30" : "Akola",
	"MH31" : "Nagpur",
	"MH32" : "Wardha",
	"MH33" : "Gadchiroli",
	"MH34" : "Chandrapur",
	"MH35" : "Gondia",
	"MH36" : "Bhandara",
	"MH37" : "Washim",
	"MH38" : "Hingoli",
	"MH39" : "Nandurbar",
	"MH40" : "Nagpur",
	"MH41" : "Malegaon",
	"MH43" : "Mumbai",
	"MH44" : "Beed",
	"MH45" : "Solapur",
	"MH46" : "Khopoli",
	"MH47" : "Mumbai",
	"MH48" : "Palghar",
	"MH49" : "Nagpur",
	"MH50" : "Satara",
	"MH51" : "Nashik",
	"UT01" : "Almora",
	"UT11" : "Chamoli",
	"UT02" : "Bageshwar",
	"UT12" : "Pauri",
	"UT03" : "Champawat",
	"UT13" : "Rudraprayag",
	"UT04" : "Nanital",
	"UT14" : "Rishikesh",
	"UT05" : "Pithoragarh",
	"UT15" : "Kotdwar",
	"UT06" : "Udham Singh Nagar",
	"UT16" : "Vikasnagar",
	"UT07" : "Dehradun",
	"UT17" : "Roorkee",
	"UT08" : "Haridwar",
	"UT18" : "Kashipur",
	"UT09" : "Tehri",
	"UT19" : "Ramnagar",
	"UT10" : "Uttarkashi",
	"UT20" : "Ranikhet",
	"AP02" : "Anantapur",
	"AP03" : "Chittoor",
	"AP04" : "YSR Kadapa",
	"AP05" : "East Godavari",
	"AP06" : "East Godavari",
	"AP07" : "Guntur",
	"AP08" : "Guntur",
	"AP18" : "Krishna",
	"AP21" : "Kurnool",
	"AP26" : "Nellore",
	"AP27" : "Prakasam",
	"AP30" : "Srikakulam",
	"AP31" : "Visakhapatnam",
	"AP32" : "Visakhapatnam",
	"AP33" : "Visakhapatnam",
	"AP34" : "Visakhapatnam",
	"AP35" : "Vizianagaram",
	"AP37" : "West Godavari",
	"AP39" : "Kadapa",
	"WB01" : "Kolkata",
	"WB02" : "Kolkata",
	"WB03" : "Kolkata",
	"WB04" : "Kolkata",
	"WB05" : "Kolkata",
	"WB06" : "Kolkata",
	"WB07" : "Kolkata",
	"WB08" : "Kolkata",
	"WB11" : "Howrah",
	"WB12" : "Howrah",
	"WB13" : "Uluberia",
	"WB14" : "Uluberia",
	"WB15" : "Hoogly",
	"WB16" : "Hoogly",
	"WB17" : "Hooghly",
	"WB18" : "Dankuni",
	"WB19" : "Alipore",
	"WB20" : "Alipore",
	"WB23" : "Barrackpore",
	"WB24" : "Barrackpore",
	"WB25" : "Barasat",
	"WB26" : "Barasat",
	"WB29" : "Tamluk",
	"WB30" : "Tamluk",
	"WB31" : "Contai",
	"WB32" : "Contai",
	"WB33" : "Midnapur",
	"WB34" : "Midnapur",
	"WB36" : "Midnapur",
	"WB37" : "Asansol",
	"WB38" : "Asansol",
	"WB39" : "Durgapur",
	"WB40" : "Durgapur",
	"WB41" : "Burdwan",
	"WB42" : "Burdwan",
	"WB43" : "Kalna",
	"WB44" : "Asansol",
	"WB47" : "Bolpur",
	"WB48" : "Bolpur",
	"WB51" : "Nadia",
	"WB52" : "Nadia",
	"WB53" : "Birbhum",
	"WB54" : "Birbhum",
	"WB55" : "Purulia",
	"WB56" : "Purulia",
	"WB57" : "Murshidabad",
	"WB58" : "Murshidabad",
	"WB59" : "Raiganj",
	"WB60" : "Raiganj",
	"WB61" : "Balurghat",
	"WB62" : "Balurghat",
	"WB63" : "Cooch Behar",
	"WB64" : "Cooch Behar",
	"WB65" : "Malda",
	"WB66" : "Malda",
	"WB67" : "Bankura",
	"WB68" : "Bankura",
	"WB69" : "Alipurduar",
	"WB70" : "Alipurduar",
	"WB71" : "Jalpaiguri",
	"WB72" : "Jalpaiguri",
	"WB73" : "Siliguri",
	"WB74" : "Siliguri",
	"WB76" : "Darjeeling",
	"WB77" : "Darjeeling",
	"WB78" : "Kalimpong",
	"WB79" : "Kalimpong",
	"WB82" : "Raghunathpur",
	"WB85" : "Mathabhanga",
	"WB86" : "Mathabhanga ",
	"WB89" : "Kalyani",
	"WB90" : "Kalyani",
	"WB91" : "Islampur",
	"WB92" : "Islampur",
	"WB93" : "Jahangirpur",
	"WB94" : "Jahangirpur",
	"WB96" : "Baruipur",
	"TN01" : "Chennai",
	"TN02" : "Chennai",
	"TN03" : "Chennai",
	"TN04" : "Chennai",
	"TN05" : "Chennai",
	"TN06" : "Chennai",
	"TN07" : "Chennai",
	"TN09" : "Chennai",
	"TN10" : "Chennai",
	"TN11" : "Chennai",
	"TN12" : "Chennai",
	"TN13" : "Chennai",
	"TN14" : "Chennai",
	"TN15" : "Chennai",
	"TN16" : "Chennai",
	"TN18" : "Chennai",
	"TN19" : "Chengalpattu",
	"TN20" : "Tiruvallur",
	"TN21" : "Kanchipuram",
	"TN22" : "Meenambakkam",
	"TN23" : "Vellore",
	"TN24" : "Krishnagiri",
	"TN25" : "Thiruvannamalai",
	"TN27" : "Salem",
	"TN28" : "Namakkal",
	"TN29" : "Dharmapuri",
	"TN30" : "Salem",
	"TN31" : "Cuddalore",
	"TN32" : "Villupuram",
	"TN33" : "Erode",
	"TN34" : "Thiruchengode",
	"TN36" : "Gobichettipalayam",
	"TN37" : "Coimbatore",
	"TN38" : "Coimbatore",
	"TN39" : "Tiruppur",
	"TN40" : "Mettupalayam",
	"TN41" : "Pollachi",
	"TN42" : "Tiruppur",
	"TN43" : "Udagamandalam",
	"TN45" : "Tiruchirappalli",
	"TN46" : "Perambalur",
	"TN47" : "Karur",
	"TN48" : "Srirangam",
	"TN49" : "Thanjavur",
	"TN50" : "Tiruvarur",
	"TN51" : "Nagapattinam",
	"TN52" : "Sankagiri",
	"TN54" : "Salem",
	"TN55" : "Pudukkottai",
	"TN56" : "Perundurai",
	"TN57" : "Dindigul",
	"TN58" : "Madurai",
	"TN59" : "Madurai",
	"TN60" : "Theni",
	"TN61" : "Ariyalur",
	"TN63" : "Sivagangai",
	"TN64" : "Madurai",
	"TN65" : "Ramanathapuram",
	"TN66" : "Coimbatore",
	"TN67" : "Virudhunagar",
	"TN68" : "Kumbakonam",
	"TN69" : "Thoothukkudi",
	"TN70" : "Hosur",
	"TN72" : "Tirunelveli",
	"TN73" : "Ranipet",
	"TN74" : "Nagercoil",
	"TN75" : "Kanniyakumari",
	"TN76" : "Tenkasi",
	"TN77" : "Attur",
	"TN78" : "Dharapuram",
	"TN79" : "Sankarankovil",
	"TN81" : "Tiruchirappalli",
	"TN82" : "Mayiladuthurai",
	"TN83" : "Tirupathur",
	"TN84" : "Srivilliputhur",
	"TN85" : "Kundrathur",
	"TN86" : "Erode",
	"TN88" : "Namakkal",
	"TN90" : "Salem",
	"TN91" : "Chidambaram",
	"TN92" : "Thiruchendur",
	"TN99" : "Coimbatore",
	}
	return dists[passing]