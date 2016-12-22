import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
x = [200000,195023.53894723748, 155672.63542790848, 135976.00739438162, 120873.16751374271, 118858.91023506956, 115758.97177099746, 106137.93874552623, 103793.64779668348, 100498.50741320696, 97474.1752023217, 95709.88916456429, 93883.70751320204, 92421.29813531431, 91198.81052245009, 90166.43780063598, 89412.45934648614, 88099.80182523477, 85507.10617008945, 84428.54491547152, 84003.20489341684, 82788.14595975104, 81762.00146481456, 81141.54220980166, 80102.06041220615, 79070.8111903254, 78370.10857904152, 77080.98918203663, 77558.90625897031, 78445.16137793439, 76155.803634123, 75293.2410356088, 74833.90810753645, 74011.76340321937, 73695.69568764848, 73343.94135026337, 72916.39921808665, 73321.11546635124, 72697.81419785526, 71913.98452164241, 71248.18567105946, 70718.56821359854, 70495.23918718053, 70530.8527527312, 69568.31932896141, 69326.91905654648, 68947.27763554685, 68694.95999358612, 68577.84395180063, 67894.54621105429]
a = [68646.62365213338, 67621.12255298805, 67213.17639668011, 67735.0631265721, 66548.40425304008, 66330.17962722965, 65802.07199493976, 66193.7874581683, 66211.40502488824, 65322.13422993849, 64893.37060648141, 64447.45878764595, 64919.06318147568, 64504.502203742144, 63836.623215267435, 63964.94301577056, 63277.39450198988, 64178.030247253846, 63521.997432833785, 62770.63966662346, 62793.62590955825, 62745.142965550396, 62775.60253474112, 62173.19680043735, 62095.83051304614, 61985.97174895569, 61748.53698738086, 62703.57993395769, 61320.15219874481, 60702.91844656915, 60804.10488614918, 61158.150813722445, 61036.18151559133, 60614.998798106215, 60532.67516372116, 60418.902050998426, 60281.68257410374, 59897.46538148773, 59981.428309134004, 59679.41592716167, 59444.2359438597, 58855.15865604686, 58789.00467182201, 58948.33846275708, 59586.83934251096, 58876.669573256564, 58903.38840965999, 58937.12672786428, 58502.231578751955, 58162.93838986066, 58452.77357085932, 58128.48351771512, 58283.13096027841, 57817.7705353479, 57672.92779257766, 57818.45966626556, 57898.27861373933, 57595.29394412114, 57593.70015471259, 57555.66344537069, 57060.980245967075, 56922.99190424408, 57179.4132762774, 56683.335498764354, 57460.487007507196, 56731.96484486615, 56568.11937508544, 56626.961405818576, 56444.10142135178, 56541.80526163813, 56213.74278707139, 55954.788485560675, 56177.18158286578, 55965.874107634525, 55890.32210929215, 55649.29044778983, 55783.55174900861, 55331.955633455116, 55736.83706586479, 55270.17742955031, 55299.56657457508, 55487.49192402944, 55564.25565038734, 55077.55456312397, 55240.49128622265, 55232.491808803665, 54894.03842584913, 55727.118549150866, 54789.0122660542, 54447.96807049795, 54486.20722695914, 54416.86590001806, 54206.24536417229, 54121.26563555656, 54361.521666417786, 54128.37377886582, 54165.69280078284, 54039.862144763036, 54306.54056837625, 53918.657283105735]
x += a
sns.set(color_codes=True)
sns.tsplot(data=x)
plt.xlabel("k")
plt.ylabel("Error")
sns.plt.show()