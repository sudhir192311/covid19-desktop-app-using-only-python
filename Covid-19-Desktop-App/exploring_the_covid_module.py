from covid import Covid

covid = Covid()
#Test 1
#print(covid.get_data())

#Test 2
#place =  covid.list_countries()
#print(place)

#Test3
#italy_cases =  covid.get_status_by_country_name("italy")
#print(italy_cases)

#Test4
#active =  covid.get_total_active_cases()
#print(active)

#Test 5: data source

covid1 = Covid(source="worldometers")
confirmed1 = covid.get_total_confirmed_cases()

print("Worldometers : "+str(confirmed1))

covid2 = Covid(source="john_hopkins")
confirmed2 = covid.get_total_confirmed_cases()

print("John Hopkins : "+str(confirmed2))