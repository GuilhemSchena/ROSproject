# ROSproject

Bonjour les amis
Nous faisons un projet de ROS avec l'UV LARM en P4.
Materna Jean-Louis
Schena Guilhem
Groupe 007

## Processus d'installation général

* Créer un nouveau projet Kinetic
* Importer et compiler le simulation_ws des professeurs : https://github.com/ceri-num/LARM-RDS-Simulation-WS
* Répeter le processus pour le catkin_ws du projet
* Pour chaque projet, une démo est disponible avec la commande suivante.

### Challenge 1:

Lancer la commande suivante, puis le téléop pour controller le robot.

````
launch student_pkg 1_navigation.launch
````

### Challenge 2:

Lancer la commande suivante, le téléop pour controller le robot, et ouvrir l'interface graphique linux intégrée pour observer la détection des bouteilles sur l'interface graphique intégrée !

````
launch student_pkg 2_mapping.launch
````

Il est également possible d'observer la détection d'objets en temps réel dans la WebShell avec commande :
````
rostopic echo /objects
````

### Commandes utiles:

````
roslaunch rviz rviz
roslaunch turtlebot_teleop keyboard_teleop.launch
````
