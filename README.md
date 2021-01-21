# ROSproject

Nous faisons un projet de ROS avec l'UV LARM en P4.
Materna Jean-Louis
Schena Guilhem
Groupe 007

## Processus d'installation général

* Créer un nouveau projet Kinetic
* Importer et compiler le simulation_ws des professeurs : https://github.com/ceri-num/LARM-RDS-Simulation-WS :

````
rm -fr simulation_ws
git clone https://github.com/ceri-num/LARM-RDS-Simulation-WS.git simulation_ws
cd simulation_ws
catkin_make
source devel/setup.bash
````

* Répeter le processus pour le catkin_ws du projet

````
rm -fr catkin_ws
git clone https://github.com/GuilhemSchena/ROSproject catkin_ws
cd catkin_ws
catkin_make
source devel/setup.bash
````

* Pour chaque projet, une démo est disponible avec la commande suivante.

### Challenge 1:

Lancer la commande suivante (qui lance aussi le challenge-1.launch), puis le téléop pour contrôler le robot. 

````
roslaunch student_pkg 1_navigation.launch
````
````
roslaunch turtlebot_teleop keyboard_teleop.launch
````

Ouvrir rviz et la configuration localization.rviz

````
roslaunch rviz rviz
````

Localiser le robot sur la carte avec l'outil 2D pose estimate. Vous pouvez envoyer des positions à atteindre avec l'outil 2D Nav Goal.
Vous pouvez aussi afficher les local et global maps en cochant la case dans rviz.

### Challenge 2:

Lancer la commande suivante, le téléop pour contrôler le robot, et ouvrir l'interface graphique linux intégrée pour observer la détection des bouteilles sur l'interface graphique intégrée !

````
roslaunch student_pkg 2_mapping.launch
````

Vous pouvez lancer Rviz et charger la configuration (PRECISER LAQUELLLLE)
````
roslaunch rviz rviz
````
Grâce à l'outil 2D Nav Goal, vous pouvez définir une destination à atteindre.

Il est également possible d'observer la détection d'objets en temps réel dans la WebShell avec commande :
````
rostopic echo /objects
````

Vous pouvez enfin enregistrer la carte avec la commande :
````
rosrun map_server map_saver -f name_of_map
````


### Challenge 3:

Lancer challenge-3.launch :
````
roslaunch larm challenge-3.launch
````

Lancer 3_exploration.launch :
````
roslaunch student_pkg 3_exploration.launch
````

Vous pouvez lancer Rviz et charger la configuration (PRECISER LAQUELLLLE)
````
roslaunch rviz rviz
````


### Commandes utiles:

````
roslaunch rviz rviz
roslaunch turtlebot_teleop keyboard_teleop.launch
````
