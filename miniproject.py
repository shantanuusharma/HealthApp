import xlrd  
import gi 
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab
from itertools import groupby 
gi.require_version('Gtk', '3.0') 
from gi.repository import Gtk, Pango,Gdk
import numpy as np


class MyWindow(Gtk.Window):
    def __init__(self):
        self.init_database()
        Gtk.Window.__init__(self, title="Health App")
        self.set_default_size(1000, 500)
        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.create_buttons()
        self.create_box()
   


    def init_database(self):
        self.database = []
        
    def create_buttons(self):
        
        bvwr = Gtk.Button.new_with_label("BMI vs water")
        bvwr.connect("clicked", self.on_bvwr_clicked)
	        
	self.grid.attach(bvwr, 0, 12, 1, 1)
        
        bvm = Gtk.Button.new_with_label("BMI vs meals")
        bvm.connect("clicked", self.on_bvm_clicked)
        self.grid.attach(bvm, 1, 12, 1, 1)
         
        mvw = Gtk.Button.new_with_label("Meals vs Water")
        mvw.connect("clicked", self.on_mvw_clicked)
        self.grid.attach(mvw, 2, 12, 1, 1)
        
        svb = Gtk.Button.new_with_label("Sex vs BMI")
        svb.connect("clicked", self.on_svb_clicked)
        self.grid.attach(svb, 3, 12, 1, 1)
        
        bvh = Gtk.Button.new_with_label("BMI vs Height")
        bvh.connect("clicked", self.on_bvh_clicked)
        self.grid.attach(bvh, 4, 12, 1, 1)
        
        bvw = Gtk.Button.new_with_label("BMI vs Weight")
        bvw.connect("clicked", self.on_bvw_clicked)
        self.grid.attach(bvw, 5, 12, 1, 1)
        
        wvp = Gtk.Button.new_with_label("Water vs Activity")
        wvp.connect("clicked", self.on_wvp_clicked)
        self.grid.attach(wvp, 5, 12, 1, 1)
        
        svp = Gtk.Button.new_with_label("Sleep vs Activity")
        svp.connect("clicked", self.on_svp_clicked)
        self.grid.attach(svp, 0, 13, 1, 1)
        
        tvs = Gtk.Button.new_with_label("Time vs Satisfaction")
        tvs.connect("clicked", self.on_tvs_clicked)
        self.grid.attach(tvs, 1, 13, 1, 1)
        
        ivs = Gtk.Button.new_with_label("Intensity vs Satisfaction")
        ivs.connect("clicked", self.on_ivs_clicked)
        self.grid.attach(ivs, 2, 13, 1, 1)
        
        tvi = Gtk.Button.new_with_label("Time vs Intensity")
        tvi.connect("clicked", self.on_tvi_clicked)
        self.grid.attach(tvi, 3, 13, 1, 1)
        
        wvt = Gtk.Button.new_with_label("Water vs Time")
        wvt.connect("clicked", self.on_wvt_clicked)
        self.grid.attach(wvt, 4, 13, 1, 1)
        
        view = Gtk.Button.new_with_label("Import")
        view.connect("clicked", self.on_import_clicked)
        self.grid.attach(view, 0, 14, 1, 1)
        
        save = Gtk.Button.new_with_label("Save")
        save.connect("clicked", self.on_save_clicked)
        self.grid.attach(save, 1, 14, 1, 1)

        okay = Gtk.Button.new_with_label("Get Analysis")
        okay.connect("clicked", self.on_info_clicked)
        self.grid.attach(okay, 2, 14, 1, 1)

        quit = Gtk.Button.new_with_label("Quit")
        quit.connect("clicked", Gtk.main_quit)
        self.grid.attach(quit, 3, 14, 1, 1)

        sex = Gtk.Button.new_with_label("Analyze")
        sex.connect("clicked", self.on_sex_clicked)
        self.grid.attach(sex, 5, 1, 1, 1)
        
        age = Gtk.Button.new_with_label("Analyze")
        age.connect("clicked", self.on_age_clicked)
        self.grid.attach(age, 5, 2, 1, 1)
        
        height = Gtk.Button.new_with_label("Analyze")
        height.connect("clicked", self.on_height_clicked)
        self.grid.attach(height, 5, 3, 1, 1)
        
        weight = Gtk.Button.new_with_label("Analyze")
        weight.connect("clicked", self.on_weight_clicked)
        self.grid.attach(weight, 5, 4, 1, 1)
        
        meals = Gtk.Button.new_with_label("Analyze")
        meals.connect("clicked", self.on_meals_clicked)
        self.grid.attach(meals, 5, 5, 1, 1)
        
        water = Gtk.Button.new_with_label("Analyze")
        water.connect("clicked", self.on_water_clicked)
        self.grid.attach(water, 5, 6, 1, 1)
        
        workout = Gtk.Button.new_with_label("Analyze")
        workout.connect("clicked", self.on_workout_clicked)
        self.grid.attach(workout, 5, 7, 1, 1)
        
        intensity = Gtk.Button.new_with_label("Analyze")
        intensity.connect("clicked", self.on_intensity_clicked)
        self.grid.attach(intensity, 5, 8, 1, 1)

        sleep = Gtk.Button.new_with_label("Analyze")
        sleep.connect("clicked", self.on_sleep_clicked)
        self.grid.attach(sleep, 5, 9, 1, 1)
        
        content = Gtk.Button.new_with_label("Analyze")
        content.connect("clicked", self.on_content_clicked)
        self.grid.attach(content, 5, 10, 1, 1)
            
    def create_box(self):
        self.sex = Gtk.ListStore(str)
        self.sex.append(["Male"])
        self.sex.append(["Female"])
        self.sex.append(["Others"])
        label = Gtk.Label("Sex  : In graphs, Red - Female and Blue - Male", xalign=0)
        self.sex_menu = Gtk.ComboBox.new_with_model(self.sex)
        self.sex_menu.connect("changed", self.on_sex_combo_changed)
        renderer_text = Gtk.CellRendererText()
        self.sex_menu.pack_start(renderer_text, True)
        self.sex_menu.add_attribute(renderer_text, "text", 0)
        self.sex_menu.set_active(0) 
        self.grid.attach(label, 0, 1, 4, 1)
        self.grid.attach(self.sex_menu, 4, 1, 2, 1)

        self.age = Gtk.ListStore(str)
        for i in range(0,111):
	        self.age.append([str(i)])
        label = Gtk.Label("How old are you?", xalign=0)
        self.age_menu = Gtk.ComboBox.new_with_model(self.age)
        self.age_menu.connect("changed", self.on_sex_combo_changed)
        renderer_text = Gtk.CellRendererText()
        self.age_menu.pack_start(renderer_text, True)
        self.age_menu.add_attribute(renderer_text, "text", 0)
        self.age_menu.set_active(20) 
        self.grid.attach(label, 0, 2, 4, 1)
        self.grid.attach(self.age_menu, 4, 2, 2, 1)
        
        self.height = Gtk.ListStore(str)
        for i in range(0,210):
	        self.height.append([str(i)])
        label = Gtk.Label("What is your height?", xalign=0)
        self.height_menu = Gtk.ComboBox.new_with_model(self.height)
        self.height_menu.connect("changed", self.on_height_combo_changed)
        renderer_text = Gtk.CellRendererText()
        self.height_menu.pack_start(renderer_text, True)
        self.height_menu.add_attribute(renderer_text, "text", 0)
        self.height_menu.set_active(140) 
        self.grid.attach(label, 0, 3, 4, 1)
        self.grid.attach(self.height_menu, 4, 3, 2, 1)
        
        self.weight = Gtk.ListStore(str)
        for i in range(0,120):
	        self.weight.append([str(i)])
        label = Gtk.Label("What is your weight?", xalign=0)
        self.weight_menu = Gtk.ComboBox.new_with_model(self.weight)
        self.weight_menu.connect("changed", self.on_weight_combo_changed)
        renderer_text = Gtk.CellRendererText()
        self.weight_menu.pack_start(renderer_text, True)
        self.weight_menu.add_attribute(renderer_text, "text", 0)
        self.weight_menu.set_active(70) 
        self.grid.attach(label, 0, 4, 4, 1)
        self.grid.attach(self.weight_menu, 4, 4, 2, 1)
 
        self.meals = Gtk.ListStore(str)
        self.meals.append(["1"])
        self.meals.append(["2"])
        self.meals.append(["3"])
        self.meals.append([">3"])
        label = Gtk.Label("How many meals do you consume in a day?", xalign=0)
        self.meals_menu = Gtk.ComboBox.new_with_model(self.meals)
        self.meals_menu.connect("changed", self.on_sex_combo_changed)
        renderer_text = Gtk.CellRendererText()
        self.meals_menu.pack_start(renderer_text, True)
        self.meals_menu.add_attribute(renderer_text, "text", 0)
        self.meals_menu.set_active(2) 
        self.grid.attach(label, 0, 5, 4, 1)
        self.grid.attach(self.meals_menu, 4, 5, 2, 1)
    
        self.water = Gtk.ListStore(str)
        self.water.append(["1-2"])
        self.water.append(["2-3"])
        self.water.append(["3-4"])
        self.water.append([">4"])
        label = Gtk.Label("About how much water do you intake in a day? (in litres)", xalign=0)
        self.water_menu = Gtk.ComboBox.new_with_model(self.water)
        self.water_menu.connect("changed", self.on_water_combo_changed)
        renderer_text = Gtk.CellRendererText()
        self.water_menu.pack_start(renderer_text, True)
        self.water_menu.add_attribute(renderer_text, "text", 0)
        self.water_menu.set_active(2) 
        self.grid.attach(label, 0, 6, 4, 1)
        self.grid.attach(self.water_menu, 4, 6, 2, 1)

        self.workout = Gtk.ListStore(str)
        self.workout.append(["Nothing dedicated to 'Physical Activities'"])
        self.workout.append(["10-20 minutes"])
        self.workout.append(["20-40 minutes"])
        self.workout.append(["40-60 minutes"])
        self.workout.append([">60 minutes"])
        label = Gtk.Label("Roughly, how much time do you spend on physical activity? (sports, walking, etc.)", xalign=0)
        self.workout_menu = Gtk.ComboBox.new_with_model(self.workout)
        self.workout_menu.connect("changed", self.on_workout_combo_changed)
        renderer_text = Gtk.CellRendererText()
        self.workout_menu.pack_start(renderer_text, True)
        self.workout_menu.add_attribute(renderer_text, "text", 0)
        self.workout_menu.set_active(2) 
        self.grid.attach(label, 0, 7, 4, 1)
        self.grid.attach(self.workout_menu, 4, 7, 2, 1)
        
        self.sleep = Gtk.ListStore(str)
        self.sleep.append(["<5"])
        self.sleep.append(["6-7"])
        self.sleep.append(["7-8"])
        self.sleep.append(["8-9"])
        self.sleep.append([">9"])
        label = Gtk.Label("How many hours of sleep do you get in a day?", xalign=0)
        self.sleep_menu = Gtk.ComboBox.new_with_model(self.sleep)
        self.sleep_menu.connect("changed", self.on_sleep_combo_changed)
        renderer_text = Gtk.CellRendererText()
        self.sleep_menu.pack_start(renderer_text, True)
        self.sleep_menu.add_attribute(renderer_text, "text", 0)
        self.sleep_menu.set_active(2) 
        self.grid.attach(label, 0, 8, 4, 1)
        self.grid.attach(self.sleep_menu, 4, 8, 2, 1)
        
        self.intensity = Gtk.ListStore(str)
        for i in range(1,11):
	        self.intensity.append([str(i)])
        label = Gtk.Label("Rate the intensity of your physical activity", xalign=0)
        self.intensity_menu = Gtk.ComboBox.new_with_model(self.intensity)
        self.intensity_menu.connect("changed", self.on_intensity_combo_changed)
        renderer_text = Gtk.CellRendererText()
        self.intensity_menu.pack_start(renderer_text, True)
        self.intensity_menu.add_attribute(renderer_text, "text", 0)
        self.intensity_menu.set_active(2) 
        self.grid.attach(label, 0, 9, 4, 1)
        self.grid.attach(self.intensity_menu, 4, 9, 2, 1)
        
        
        self.content = Gtk.ListStore(str)
        self.content.append(["Yes"])
        self.content.append(["No"])
        self.content.append(["Don't Care"])
        label = Gtk.Label("Are you content with the amount of physical activity you engage in?", xalign=0)
        self.content_menu = Gtk.ComboBox.new_with_model(self.content)
        self.content_menu.connect("changed", self.on_sex_combo_changed)
        renderer_text = Gtk.CellRendererText()
        self.content_menu.pack_start(renderer_text, True)
        self.content_menu.add_attribute(renderer_text, "text", 0)
        self.content_menu.set_active(2) 
        self.grid.attach(label, 0, 10, 4, 1)
        self.grid.attach(self.content_menu, 4, 10, 2, 1)
        
        self.aware = Gtk.ListStore(str)
        self.aware.append(["Yes"])
        self.aware.append(["No"])
        label = Gtk.Label("(Optional) Are you aware of your blood pressure, sugar, cholestrol?", xalign=0)
        self.aware_menu = Gtk.ComboBox.new_with_model(self.aware)
        self.aware_menu.connect("changed", self.on_sex_combo_changed)
        renderer_text = Gtk.CellRendererText()
        self.aware_menu.pack_start(renderer_text, True)
        self.aware_menu.add_attribute(renderer_text, "text", 0)
        self.aware_menu.set_active(2) 
        self.grid.attach(label, 0, 11, 4, 1)
        self.grid.attach(self.aware_menu, 4, 11, 2, 1)
        
    def on_sex_clicked(self,button):
        plt.clf()
        labels = 'Male','Female','Others'
        male = 0
        female = 0
        others = 0
        for i in range(len(self.database)):
            if self.database[i]['sex'] == 'Male':
                male = male + 1
            elif self.database[i]['sex'] == 'Female':
	            female = female + 1
            else:
                others = others + 1
        sizes = [male,female,others]
	        
        explode = (0, 0, 0)  # explode 1st slice
        plt.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()
    
    def on_age_clicked(self,button):
        plt.clf()
        labels = []
        for i in range(len(self.database)):
	        labels.append(self.database[i]['age'])
        labels.sort()
        sizes = [len(list(group)) for key, group in groupby(labels)]
        labels = tuple(set(labels))
        explode = (0, 0, 0, 0)
        plt.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()

    def on_height_clicked(self,button):
        plt.clf()
        labels = []
        for i in range(len(self.database)):
	        labels.append(self.database[i]['height']//10)
        labels.sort()
        sizes = [len(list(group)) for key, group in groupby(labels)]
        for i in range(len(labels)):
            x = labels[i]*10
            y = x + 10
            labels[i] = str(x) + '-' + str(y)
        labels = tuple(set(labels))
        plt.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()
    
    def on_weight_clicked(self,button):
        plt.clf()
        labels = []
        for i in range(len(self.database)):
	        labels.append(self.database[i]['weight']//10)
        labels.sort()
        sizes = [len(list(group)) for key, group in groupby(labels)]
        for i in range(len(labels)):
            x = labels[i]*10
            y = x + 10
            labels[i] = str(x) + '-' + str(y)
        labels = tuple(set(labels))
        plt.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()

    def on_meals_clicked(self,button):
        plt.clf()
        labels = []
        for i in range(len(self.database)):
	        labels.append(str(self.database[i]['meals']))
        labels.sort()
        sizes = [len(list(group)) for key, group in groupby(labels)]
        labels = tuple(set(labels))
        plt.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()
    
    def on_water_clicked(self,button):
        plt.clf()
        labels = []
        for i in range(len(self.database)):
	        labels.append(str(self.database[i]['water']))
        labels.sort()
        sizes = [len(list(group)) for key, group in groupby(labels)]
        labels = tuple(set(labels))
        plt.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()

    
    def on_workout_clicked(self,button):
        plt.clf()
        labels = []
        for i in range(len(self.database)):
	        labels.append(str(self.database[i]['workout']))
        labels.sort()
        sizes = [len(list(group)) for key, group in groupby(labels)]
        labels = tuple(set(labels))
        plt.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()
    
    def on_intensity_clicked(self,button):
        plt.clf()
        labels = []
        for i in range(len(self.database)):
	        labels.append(str(self.database[i]['intensity']))
        labels.sort()
        sizes = [len(list(group)) for key, group in groupby(labels)]
        labels = tuple(set(labels))
        plt.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()
 
    def on_sleep_clicked(self,button):
        plt.clf()
        labels = []
        for i in range(len(self.database)):
	        labels.append(str(self.database[i]['sleep']))
        labels.sort()
        sizes = [len(list(group)) for key, group in groupby(labels)]
        labels = tuple(set(labels))
        plt.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()
 
    def on_content_clicked(self,button):
        plt.clf()
        labels = []
        for i in range(len(self.database)):
	        labels.append(str(self.database[i]['content']))
        labels.sort()
        sizes = [len(list(group)) for key, group in groupby(labels)]
        labels = tuple(set(labels))
        plt.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()
                        
 
    

    def on_bvwr_clicked(self,button):
	plt.clf()
	mwater = []
	fwater = []
	mbmi = []
	fbmi = []
        for i in range(len(self.database)):
            if(self.database[i]['sex'] == 'Male'):
                x = self.database[i]['water']
                if x == '>4':
                    x = '4.5'
                else:
                    x = str(int(x[0]) + 0.5)
                mwater.append(x)	
                mbmi.append(self.database[i]['bmi'])			
            else:
                x = self.database[i]['water']
                if x == '>4':
                    x = '4.5'
                else:
                    x = str(int(x[0]) + 0.5)
                fwater.append(x)	
                fbmi.append(self.database[i]['bmi'])
        plt.plot(mwater, mbmi, 'bo') #(x,y,bo color)
        plt.plot(fwater, fbmi, 'ro')
        plt.axis('equal')
        plt.show()
        return

	


    def on_bvm_clicked(self,button):
        plt.clf() #pops new screen
        mmeal = [] 
        fmeal = []
        mbmi = []
        fbmi = [] 
        for i in range(len(self.database)):
            if(self.database[i]['sex'] == 'Male'):
                x = self.database[i]['meals']
                if x == '>3':
	                x = 4
                else:
                	x = str(x)                
		mmeal.append(x)
                mbmi.append(self.database[i]['bmi'])
            else:
                x = self.database[i]['meals']
                if x == '>3':
	                x = 4
                else:
                	x = str(x)                
		fmeal.append(x)
                fbmi.append(self.database[i]['bmi'])
	            
        plt.plot(mmeal, mbmi, 'bo') #(x,y,bo color)
        plt.plot(fmeal, fbmi, 'ro')
        plt.axis('equal')
        plt.show()
        return
        
    def on_mvw_clicked(self, button): 
        plt.clf()
        mmeal = []
        fmeal = []
        mwater = []
        fwater = [] 
        for i in range(len(self.database)):
            if(self.database[i]['sex'] == 'Male'):
                x = self.database[i]['meals']
                if x == '>3':
	                x = 4.5
                else: 
			x = str(x)
                mmeal.append(x)
                y = self.database[i]['water']
                if y == '>4':
                	y = '4.5'
                else:
                	y = str(int(y[0]) + 0.5)
                mwater.append(y)
            else:
                x = self.database[i]['meals']
                if x == '>3':
			x = 4.5
                else:
			x = str(x)
                fmeal.append(x)
                y = self.database[i]['water']
                if y == '>4':
                	y = '4.5'
                else:
                	y = str(int(y[0]) + 0.5)
                fwater.append(y)
	            
        plt.plot(mmeal, mwater, 'bo')
        plt.plot(fmeal, fwater, 'ro')
        plt.axis('equal')
        plt.show()
        return  
    def on_svb_clicked(self, button):
	plt.clf()	
	mbmi = []
	mgender = []
	fgender = []	
	fbmi = []
	for i in range(len(self.database)):
            if(self.database[i]['sex'] == 'Male'):
                mbmi.append(self.database[i]['bmi'])
                x = self.database[i]['sex']
		x = '1';		
		mgender.append(x)              
	    else:
                fbmi.append(self.database[i]['bmi'])
                y = self.database[i]['sex']
		y = '2';		
		fgender.append(y)                               
	plt.plot(mgender, mbmi, 'bo')
        plt.plot(fgender, fbmi, 'ro')
        plt.axis('equal')
        plt.show()
        return  
    def on_bvw_clicked(self, button):
        plt.clf()
        mweight = []
        fweight = []
        mbmi = []
        fbmi = [] 
        for i in range(len(self.database)):
            if(self.database[i]['sex'] == 'Male'):
                mweight.append(self.database[i]['weight'])
                mbmi.append(self.database[i]['bmi'])
            else:
                fweight.append(self.database[i]['weight'])
                fbmi.append(self.database[i]['bmi'])
	            
        plt.plot(mweight, mbmi, '-bo')
        plt.plot(fweight, fbmi, '-ro')
        plt.axis('equal')
        plt.show()    
        
    def on_bvh_clicked(self, button): 
        plt.clf()
        mheight = []
        fheight = []
        mbmi = []
        fbmi = [] 
        for i in range(len(self.database)):
            if(self.database[i]['sex'] == 'Male'):
                mheight.append(self.database[i]['height'])
                mbmi.append(self.database[i]['bmi'])
            else:
                fheight.append(self.database[i]['height'])
                fbmi.append(self.database[i]['bmi'])
        mheight.sort()
        plt.plot(mheight, mbmi, '-bo')
        plt.plot(fheight, fbmi, '-ro')
        plt.axis('equal')
        plt.show()
    def on_wvt_clicked(self,button):
        plt.clf()
        mwater = []
        fwater = []
        mpa = []
        fpa = [] 
        for i in range(len(self.database)):
            if(self.database[i]['sex'] == 'Male'):
                x = self.database[i]['water']
                if x == '>4':
                    x = '4.5'
                else:
                    x = str(int(x[0]) + 0.5)
                mwater.append(x)
                y = self.database[i]['workout']
                if y[0] == 'M':
	                y = '80'
                if y[0] == 'N':
                    y = '0'
                if y[0] == '1':
                    y = '10'
                if y[0] == '2':
                    y = '30'
                if y[0] == '4':
                    y = '50'
                mpa.append(y)
            else:
                x = self.database[i]['water']
                if x == '>4':
                    x = '4.5'
                else:
                    x = str(int(x[0]) + 0.5)
                fwater.append(x)
                y = self.database[i]['workout']
                if y[0] == 'M':
	                y = '80'
                if y[0] == 'N':
                    y = '0'
                if y[0] == '1':
                    y = '10'
                if y[0] == '2':
                    y = '30'
                if y[0] == '4':
                    y = '50'
                fpa.append(y)
        mwater.sort()
        fwater.sort()
        plt.plot(mwater, mpa, 'bo')
        plt.plot(fwater, fpa, 'ro')
        plt.axis('equal')
        plt.show()
	return
        
    def on_svp_clicked(self, button): 
        plt.clf()
        msleep = []
        fsleep = []
        mpa = []
        fpa = [] 
        for i in range(len(self.database)):
            if(self.database[i]['sex'] == 'Male'):
                x = self.database[i]['sleep']
                if x == '>9':
                	x = '9.5'
		if x == '<5':
			x = '4.5'
                else:
                	x = str(x[0])
                msleep.append(x)
	        y = self.database[i]['workout']
                if y[0] == 'M':
	                y = '80'
                if y[0] == 'N':
                    y = '0'
                if y[0] == '1':
                    y = '10'
                if y[0] == '2':
                    y = '30'
                if y[0] == '4':
                    y = '50'
                
		#y = (int(y))*(self.database[i]['intensity'])
		mpa.append(y)
            else:
                x = self.database[i]['sleep']
                if x == '>9':
                	x = '9.5'
		if x == '<5':
			x = '4.5'
                else:
                	x = str(x[0])
                fsleep.append(x)
	        y = self.database[i]['workout']
                if y[0] == 'M':
	                y = '80'
                if y[0] == 'N':
                    y = '0'
                if y[0] == '1':
                    y = '10'
                if y[0] == '2':
                    y = '30'
                if y[0] == '4':
                    y = '50'
                
		#y = (int(y))*(self.database[i]['intensity'])
		fpa.append(y)
        msleep.sort()
        fsleep.sort()
        plt.plot(msleep, mpa, 'bo')
        plt.plot(fsleep, fpa, 'ro')
        plt.axis('equal')
        plt.show()
        return

    def on_tvs_clicked(self, button):
        plt.clf()
	ms = []
	fs = []       	
	mpa = []
        fpa = [] 
        for i in range(len(self.database)):
            if(self.database[i]['sex'] == 'Male'):
                x = self.database[i]['aware']
                if x[0] == 'Y':
                    x = '30'
                if x[0] == 'N':
		    x = '40'
		if x[0] == 'D':
		    x = '50'	
                ms.append(x)
                y = self.database[i]['workout']
                if y[0] == 'M':
	                y = '80'
                if y[0] == 'N':
                    y = '0'
                if y[0] == '1':
                    y = '10'
                if y[0] == '2':
                    y = '30'
                if y[0] == '4':
                    y = '50'
                mpa.append(y)
            else:
            
                x = self.database[i]['aware']
                if x[0] == 'Y':
                    x = '30'
                if x[0] == 'N':
		    x = '40'
		if x[0] == 'D' :
		    x = '50'	
                fs.append(x)               
                y = self.database[i]['workout']
                if y[0] == 'M':
	                y = '80'
                if y[0] == 'N':
                    y = '0'
                if y[0] == '1':
                    y = '10'
                if y[0] == '2':
                    y = '30'
                if y[0] == '4':
                    y = '50'
                fpa.append(y)
        ms.sort()
        fs.sort()
        plt.plot(ms, mpa, 'bo')
        plt.plot(fs, fpa, 'ro')
        plt.axis('equal')
        plt.show()	 
        return
 
    def on_ivs_clicked(self,button): 
        plt.clf()
	ms = []
	fs = []       	
	mi = []
        fi = [] 
        for i in range(len(self.database)):
            if(self.database[i]['sex'] == 'Male'):
                x = self.database[i]['aware']
                if x[0] == 'Y':
                    x = '30'
                if x[0] == 'N':
		    x = '40'
		if x[0] == 'D':
		    x = '50'	
                ms.append(x)
                y = self.database[i]['intensity']
                y = str(y)
		mi.append(y)      
            else:
            
                x = self.database[i]['aware']
                if x[0] == 'Y':
                    x = '30'
                if x[0] == 'N':
		    x = '40'
		if x[0] == 'D' :
		    x = '50'	
                fs.append(x)               
                y = self.database[i]['intensity']
                y = str(y)
		fi.append(y) 
                
        mi.sort()
        fi.sort()
        plt.plot(mi, ms, 'bo')
        plt.plot(fi, fs, 'ro')
        plt.axis('equal')
	plt.show()
	return

    def on_tvi_clicked(self, button): 
        plt.clf()
        mi = []
        fi = []
        mpa = []
        fpa = [] 
        for i in range(len(self.database)):
            if(self.database[i]['sex'] == 'Male'):
                x = self.database[i]['intensity']
                x = str(x)
		mi.append(x)   
                y = self.database[i]['workout']
                if y[0] == 'M':
	                y = '80'
                if y[0] == 'N':
                    y = '0'
                if y[0] == '1':
                    y = '10'
                if y[0] == '2':
                    y = '30'
                if y[0] == '4':
                    y = '50'
                mpa.append(y)
            else:
	        x = self.database[i]['intensity']
                x = str(x)
		fi.append(x)   
                y = self.database[i]['workout']
                if y[0] == 'M':
	                y = '80'
                if y[0] == 'N':
                    y = '0'
                if y[0] == '1':
                    y = '10'
                if y[0] == '2':
                    y = '30'
                if y[0] == '4':
                    y = '50'
                fpa.append(y)
        mi.sort()
        fi.sort()
        plt.plot(mi, mpa, 'bo')
        plt.plot(fi, fpa, 'ro')
        plt.axis('equal')
	plt.show()
	return



	return
    def on_wvp_clicked(self): 
        return 
    def on_classify_clicked(self, button):
        return
    def on_import_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,Gtk.FileChooserAction.OPEN,\
        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        
        self.add_filters(dialog)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.read_data(dialog.get_filename())
        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Excel Sheets")
        filter_text.add_mime_type("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        dialog.add_filter(filter_text)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)


    def on_save_clicked(self, button):
        [start, end] = self.buffer.get_bounds()
        oquestion = self.buffer.get_text(start, end, False)
        cquestion = self.change()
        self.buffer1.set_text(cquestion)
        tree_iter = self.subconcept_menu.get_active_iter()
        
        if tree_iter != None:
            model = self.subconcept_menu.get_model()
            subconcept = model[tree_iter][0]
        
    def on_height_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        name = ""
        if tree_iter is not None:
            model = combo.get_model()
            name = model[tree_iter][0]
        self.height = name
    def on_weight_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        name = ""
        if tree_iter is not None:
            model = combo.get_model()
            name = model[tree_iter][0]
        self.weight = name
    def on_workout_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        name = ""
        if tree_iter is not None:
            model = combo.get_model()
            name = model[tree_iter][0]
        self.workout = name
    def on_sleep_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        name = ""
        if tree_iter is not None:
            model = combo.get_model()
            name = model[tree_iter][0]
        self.sleep = name
    def on_water_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        name = ""
        if tree_iter is not None:
            model = combo.get_model()
            name = model[tree_iter][0]
        self.water = name
    def on_intensity_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        name = ""
        if tree_iter is not None:
            model = combo.get_model()
            name = model[tree_iter][0]
        self.intensity = name
        
    def on_sex_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        name = ""
        if tree_iter is not None:
            model = combo.get_model()
            name = model[tree_iter][0]
    
    def read_data(self,path):
         book = xlrd.open_workbook(path)
         sheet = book.sheet_by_index(0)
         for i in range(1,sheet.nrows):
             data = {}
             data['sex'] = sheet.cell(i,0).value
             data['age'] = int(sheet.cell(i,1).value)
             data['height'] = int(sheet.cell(i,2).value)
             data['weight'] = int(sheet.cell(i,3).value)
             data['meals'] = sheet.cell(i,4).value
             data['water'] = sheet.cell(i,5).value
             data['workout'] = sheet.cell(i,6).value
             data['intensity'] = sheet.cell(i,7).value
             data['sleep'] = sheet.cell(i,8).value
             data['content'] = sheet.cell(i,9).value
             data['aware'] = sheet.cell(i,9).value
             data['bmi'] = float(data['weight'])/float((data['height']/100)**2)
             self.database.append(data)
    def on_info_clicked(self, widget):
        answer = this_function(float(self.weight)/((float(self.height)/100)**2),self.workout,int(self.intensity),self.water,self.sleep)
        dialog = Gtk.MessageDialog(self, 10, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, answer[0])
        dialog.format_secondary_text(str(answer[1]))
        dialog.run()
        dialog.destroy()
        dialog1 = Gtk.MessageDialog(self, 3, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, answer[2])
        dialog1.format_secondary_text(str(answer[3]))
        dialog1.run()
        dialog1.destroy()
        dialog2 = Gtk.MessageDialog(self, 6, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, answer[4])
        dialog2.format_secondary_text(str(answer[5]))
        dialog2.run()
        dialog2.destroy()

def this_function(bmi, duration, intensity, water, sleep):
	if duration[0] == 'N':
		duration = 0
	elif duration[0] == '1':
		duration = 1
	elif duration[0] == '2':
		duration = 2
	elif duration[0] == '3':
		duration = 3
	elif duration[0] == '4':
		duration = 4
	elif duration[0] == 'M':
		duration = 5

	if water[0] == '<':
		water = '1'
	elif water[0] == '1':
		water = 2
	elif water[0] == '2':
		water = 3
	elif water[0] == '3':
		water = 4
	elif water[0] == '>':
		water = 5

	if sleep[0] == '5':
		sleep = 5
	elif sleep[0] == '<':
		sleep = 4
	elif sleep[0] == '6':
		sleep = 6
	elif sleep[0] == '7':
		sleep = 7
	elif sleep[0] == '8':
		sleep = 8
	elif sleep[0] == '>':
		sleep = 9
	final = []

	final.append('BMI Analysis:')
	if bmi <= 18.5:
		#final.append('You are underweight.')
		if duration >= 2:
			if intensity > 4:
				final.append('You are underweight. Step down the intensity of your physical activity. You should focus on gaining weight (in the form of muscle), which could involve altering your diet such that you consume more protein.')
			else:
				final.append('You are underweight. If your activity involves building, increase its intensity and incorporate cardio occassionally. Also, consider increasing your number of meals, while decreasing their portions.')
		else:
			final.append('You are underweight. Focus on putting on some weight. You aren\'t doing anything to lose, but you need to take healthy steps towards gaining body muscle, like adapting a more protein-rich diet.')
	elif bmi > 18.5 and bmi < 25:
		if bmi > 18.5 and bmi < 20:
			#final.append('You should be careful, since you\'re nearing towards becoming underweight.')
			if duration >= 3:
				if intensity > 6:
					final.append('You should be careful, since you\'re nearing towards becoming underweight. Consider lowering the intensity of your activity, or the amount of time you spend on it.')
				else:
					final.append('You should be careful, since you\'re nearing towards becoming underweight. Make sure that your physical activity doesn\'t get more intense than it is now. Think about reducing the amount of time you\'re spending on it.')
			else:
				if intensity > 6:
					final.append('You should be careful, since you\'re nearing towards becoming underweight. Make sure that you don\'t spend more time on physical activities than you already are. Consider lowering the intensity.')
				else :
					final.append('Your BMI looks nice though there is scope for slight improvement.')
		elif bmi >= 20 and bmi < 24:
			final.append('Your BMI looks healthy. Whatever kind of physical activity you do, keep it up.')
		else:
			final.append('You should be careful, since you\'re nearing towards becoming overweight.')
			if duration >= 3:
				if intensity > 6:
					final.append('You should be careful, since you\'re nearing towards becoming overweight. You could consider stepping up the intensity of your physical activity even higher, or the duration of time spent. You could also make changes to your diet to boost your metabolism, like having smaller but more frequent meals.')
				else:
					final.append('You should be careful, since you\'re nearing towards becoming overweight. You should step up the intensity of your physical activity significantly.')
			else:
				if intensity > 6:
					final.append('You should be careful, since you\'re nearing towards becoming overweight. You should increase the amount of time you\'re spending on your physical activity significantly. Also, increase the intensity if possible.')
				else:
					final.append('You should be careful, since you\'re nearing towards becoming overweight. You should spend more time being physically active. Also, it needs to be intense for you to see changes.')
	else:
		#final.append('You\'re overweight.')
		if duration >= 2:
			if intensity > 7:
				final.append('You\'re overweight. If you\'ve just started, keep going, you will see results. If you\'ve been doing this since a long time, keep track of what you intake, and consider stepping up the time and intensity even higher.')
			else:
				final.append('You\'re overweight. You need to increase the intensity of your physical activity by a significant margin.')
		else:
			if intensity > 7:
				final.append('You\'re overweight. Increase the amount of time you\'ve been spending. If you don\'t see results, increase the intensity gradually.')
			else:
				final.append('You\'re overweight. You need to significantly work towards being physically fit. At first, step up the amount of time you\'ve been spending, and as you get comfortable, increase the intensity along with it. Also, consume fewer calories, and work towards boosting your metabolism.')

	final.append('Analysis of intake of water:')
	if water <= 1:
		if intensity*duration < 20:
			final.append('You should be consuming a little more water. Take it upto 2.5 litres a day.')
		else:
			final.append('You are probably not having enough water to compensate for your lost fluids.')
			if intensity*duration < 30:
				final.append('Take it up to 3-4 litres a day.')
			else:
				final.append('Take it up to more than 4 litres a day.')
	elif water > 1 and water <= 3:
		if intensity*duration < 20:
			final.append('You could be consuming a bit more than water than your body needs, but it won\'t hurt you in any way.')
		else:
			if intensity*duration > 30:
				final.append('Consider consuming a little more than 4 litres a day to compensate for the fluids lost because of your physical activities.')
			else:
				final.append('You seem to be having just the right amount of water.')
	else:
		if intensity*duration < 20:
			final.append('Water usually doesn\'t hurt, but it won\'t be too bad for you if you consume slightly less of it.')
		else:
			final.append('You\'re having just about the right amount of water as your body should.')
	final.append('Sleep analysis:')
	if sleep <= 5:
		final.append('You should definitely get more sleep, at least an hour more.')
		if intensity*duration > 14:
			final.append('You don\'t seem to be giving enough rest to your body, considering the energy you spend being active.')
	elif sleep > 5 and sleep <= 7:
			final.append('You\'re getting somewhat the recommended healthy number of hours of sleep.')
	else:
		final.append('You\'re sleeping a bit more than one should. It won\'t hurt lazing around a little less, yeah?')
		if intensity*duration < 12:
			if bmi > 24 or bmi < 20:
				final.append('Consider spending some time on your physical fitness.')
			else:
				final.append('Spend some of that time in doing something else. Something productive, maybe?')
	return final
'''x = input()
y = input()
z = input()
p = input()
q = input()
print(this_function(float(x), y, int(z), p, q))'''
     
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
