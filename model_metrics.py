import numpy as np

#Talent Scores: based on historic data for each track on the calendar

t_s_Bahrain = np.array([100, 40, 50, 60, 30])
t_s_Saudi = np.array([100, 40, 50, 60, 30])
t_s_Australia = np.array([100, 40, 50, 60, 30])
t_s_Azerbaizan = np.array([100, 40, 50, 60, 30])
t_s_Miami = np.array([100, 40, 50, 60, 30])
t_s_Imola = np.array([100, 40, 50, 60, 30])
t_s_Monaco = np.array([100, 40, 50, 60, 30])
t_s_Barcelona = np.array([100, 40, 50, 60, 30])
t_s_Canada = np.array([100, 40, 50, 60, 30])
t_s_Austria = np.array([100, 40, 50, 60, 30])
t_s_Silverstone = np.array([100, 40, 50, 60, 30])
t_s_Hungaroring = np.array([100, 40, 50, 60, 30])
t_s_Spa = np.array([100, 40, 50, 60, 30])
t_s_Zandvoort = np.array([100, 40, 50, 60, 30])
t_s_Monza =np.array([100, 40, 50, 60, 30])
t_s_Singapore = np.array([100, 40, 50, 60, 30])
t_s_Suzuka = np.array([100, 40, 50, 60, 30])
t_s_Qatar = np.array([100, 40, 50, 60, 30])
t_s_COTA = np.array([100, 40, 50, 60, 30])
t_s_Mexico = np.array([100, 40, 50, 60, 30])
t_s_Interlagos = np.array([100, 40, 50, 60, 30])
t_s_Vegas = np.array([100, 40, 50, 60, 30])
t_s_YasMarina = np.array([100, 40, 50, 60, 30])

#Car Performance of the given tracks

car_Bahrain = np.array([100, 100, 40, 60, 60])
car_Saudi = np.array([100, 100, 40, 60, 60])
car_Australia = np.array([100, 100, 40, 60, 60])
car_Azerbaizan = np.array([100, 100, 40, 60, 60])
car_Miami = np.array([100, 100, 40, 60, 60])
car_Imola = np.array([100, 100, 40, 60, 60])
car_Monaco = np.array([100, 100, 40, 60, 60])
car_Barcelona = np.array([100, 100, 40, 60, 60])
car_Canada = np.array([100, 100, 40, 60, 60])
car_Austria = np.array([100, 100, 40, 60, 60])
car_Silverstone = np.array([100, 100, 40, 60, 60])
car_Hungaroring = np.array([100, 100, 40, 60, 60])
car_Spa = np.array([100, 100, 40, 60, 60])
car_Zandvoort = np.array([100, 100, 40, 60, 60])
car_Monza =np.array([100, 100, 40, 60, 60])
car_Singapore = np.array([100, 100, 40, 60, 60])
car_Suzuka = np.array([100, 100, 40, 60, 60])
car_Qatar = np.array([100, 100, 40, 60, 60])
car_COTA = np.array([100, 100, 40, 60, 60])
car_Mexico = np.array([100, 100, 40, 60, 60])
car_Interlagos = np.array([100, 100, 40, 60, 60])
car_Vegas = np.array([100, 100, 40, 60, 60])
car_YasMarina = np.array([100, 100, 40, 60, 60])


#Pitstop scores for each track for each driver:

pitstop_Bahrain = np.array([100, 90, 80, 60, 60])
pitstop_Saudi = np.array([100, 90, 80, 60, 60])
pitstop_Australia = np.array([100, 90, 80, 60, 60])
pitstop_Azerbaizan = np.array([100, 90, 80, 60, 60])
pitstop_Miami = np.array([100, 90, 80, 60, 60])
pitstop_Imola = np.array([100, 90, 80, 60, 60])
pitstop_Monaco = np.array([100, 90, 80, 60, 60])
pitstop_Barcelona = np.array([100, 90, 80, 60, 60])
pitstop_Canada = np.array([100, 90, 80, 60, 60])
pitstop_Austria = np.array([100, 90, 80, 60, 60])
pitstop_Silverstone = np.array([100, 90, 80, 60, 60])
pitstop_Hungaroring = np.array([100, 90, 80, 60, 60])
pitstop_Spa = np.array([100, 90, 80, 60, 60])
pitstop_Zandvoort = np.array([100, 90, 80, 60, 60])
pitstop_Monza =np.array([100, 90, 80, 60, 60])
pitstop_Singapore = np.array([100, 90, 80, 60, 60])
pitstop_Suzuka = np.array([100, 90, 80, 60, 60])
pitstop_Qatar = np.array([100, 90, 80, 60, 60])
pitstop_COTA = np.array([100, 90, 80, 60, 60])
pitstop_Mexico = np.array([100, 90, 80, 60, 60])
pitstop_Interlagos = np.array([100, 90, 80, 60, 60])
pitstop_Vegas = np.array([100, 90, 80, 60, 60])
pitstop_YasMarina = np.array([100, 90, 80, 60, 60])


talent_score = np.vstack([t_s_Bahrain, t_s_Saudi, t_s_Australia, t_s_Azerbaizan, t_s_Miami, t_s_Imola, 
                          t_s_Monaco, t_s_Barcelona, t_s_Canada, t_s_Austria, t_s_Silverstone, t_s_Hungaroring, 
                          t_s_Spa, t_s_Zandvoort, t_s_Monza, t_s_Singapore, t_s_Suzuka, t_s_Qatar, 
                          t_s_COTA, t_s_Mexico, t_s_Interlagos, t_s_Vegas, t_s_YasMarina]).flatten()

car_performance = np.vstack([car_Bahrain, car_Saudi, car_Australia, car_Azerbaizan, car_Miami, car_Imola, 
                          car_Monaco, car_Barcelona, car_Canada, car_Austria, car_Silverstone, car_Hungaroring, 
                          car_Spa, car_Zandvoort, car_Monza, car_Singapore, car_Suzuka, car_Qatar, 
                          car_COTA, car_Mexico, car_Interlagos, car_Vegas, car_YasMarina]).flatten()


pitstop_performance = np.vstack([pitstop_Bahrain, pitstop_Saudi, pitstop_Australia, pitstop_Azerbaizan, pitstop_Miami, pitstop_Imola, 
                          pitstop_Monaco, pitstop_Barcelona, pitstop_Canada, pitstop_Austria, pitstop_Silverstone, pitstop_Hungaroring, 
                          pitstop_Spa, pitstop_Zandvoort, pitstop_Monza, pitstop_Singapore, pitstop_Suzuka, pitstop_Qatar, 
                          pitstop_COTA, pitstop_Mexico, pitstop_Interlagos, pitstop_Vegas, pitstop_YasMarina]).flatten()


X = np.column_stack([talent_score, car_performance, pitstop_performance])

#overall performance of the driver historically speaking (Drivers with longers careers obviously have a more accurate score), represented as 'y'

y = np.array([100, 50, 30, 40, 25])
y = np.vstack([y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y, y]).flatten()