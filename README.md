==Description of Core Features==

This application features the use of a TensorFlow classification model that predicts the probability of five distinct outcomes occurring given the input features (see the next section for an explaination of the data). The user can run prog.py to interact with this data by testing the model with various inputs. This file will include a menu that will include a number of options to interact with the model including, but not limited to a simulator that displays the output of the model based on input (for example, if "Fumble" has a 5% chance of occurring, there's a 5% chance that that the user is notified that a "Fumble" occurs), and a comparision of each outcome occurring for the attribute "Opponent Play". There will be more options than these. 

Inspiration for model.py: https://www.tensorflow.org/tutorials/structured_data/feature_columns

==Explaining the Data==
The model evaluates the probability of five distinct outcomes (see the Result column in "Dataset Attributess") that may occur when the Florida Gators football team's defense has forced the opposing team's offense into a third-down or fourth-down. 
Please jump to the next paragraph if you understood nothing from the past sentence and do desire to understand it. If you do not care to do so, the important takeaway is that the model predicts the outcome of a single event with "Conversion" being the negative result (unless you are rooting against the Gators), "Inconversion" being a good result, and the other three results being very good (albeit the least common) results.
Many attributes relating to, but not limited to opposing team strength, opponent position on the field (such as distance to first down and goal), and the opponent's play type on the down. The data collected is from every third and fourth down from every Florida regular season football game over the past two seasons. 
Only data from the past two seasons were used since those are the only years where Florida's current coach, Dan Mullen and defensive coordinator, Todd Grantham have been employed at the university. Using data earlier than that would not account for tendencies of previous coaching staffs and talent of individual players (Florida's overall defense has been about equal in the two most recent years. 

For those unfamiliar with the sport, an offense has four tries (called downs) to advance the ball for a combined ten yards for a first down. If the opponent fails to convert on the first three downs, they will often punt (kick the ball down the field so Florida's offense would have to start further from scoring territory) or kick a field goal (3 points as opposed to a touchdown's 6) if within range. If the opponent attempts to convert on fourth-down, stopping a conversion is even more important as the Gators offense would get the ball back in this case (as opposed to the opposing team having more changes to score a touchdown). The three results other than "Conversion" and "Non-Conversion" are all types of non-conversions that are worse for the offense than a "Non-Conversion" label. A "Sack" indicates that the opposing quarterback was tackled and lost yards for the offense, an "Interception" indicates that the opposing quarterback through a ball that was caught by a Florida defender (and therefore gave the ball to Florida), and a "Fumble" indicates that someone from the opposing offense dropped the ball while holding it and a Florida defender was able to grab it (also giving the ball to Florida). In addition to setting back the opposing team, the latter three results are "momentum" plays that energize the defense's team (Florida in this instance) and demoralize the opposing team. Achieving one of these three results is often a major goal of defenses during these important downs.

==Dataset Attributes==

Column					Description						Feature Type	Data Type
Down					3rd or 4th Down						Categorical	Integer
Score Differential			Florida Score - Opponent Score				Numerical	Integer
Current Quarter				Quarter the game is in (1,2,3,4)			Categorical	Integer
Opponent Offense 			Offense SP+ at end of season				Numerical	Double
Opponent Offense Rank			Offense SP+ Rank Among FBS Teams			Numerical	Integer
Rush Efficiency				Opponent Yards Per Rush					Numerical	Double
Rush Rank				Opponent Yards Per Rush Rank Among FBS Teams		Numerical	Integer
Pass Efficiency				Opponent Yards Per Pass Atempt				Numerical	Double
Pass Rank				Opponent Yards Per Pass Atempt Rank Among FBS Teams	Numerical	Integer
Rush Grade				Opponent Offense SP+ Rank + Yards Per Rush		Numerical	Integer
Pass Grade				Opponent Offense SP+ Rank + Yards Per Pass Attempt	Numerical	Integer
Opponent Play				Run or Pass						Categorical	String
Yards-To-Go				3rd-and-?						Numerical	Integer
Yards-To-Goal				# of yards away from touchdown				Numerical	Integer
Number of Yards Gained			Likely won't be utilized				Numerical	Integer
Location				Away, Neutral, Home					Categorical	String
Result					Conversion,Non-Conversion,Sack,Interception,Fumble	Categorical	String

==Important Files Contained in Repository==

prog.py - File where the model can be interacted with. Only file that needs to be run.
> python prog.py
model.py - File where model is to be created and trained.
> python model.py
> requires 1. numpy, 2. pandas, 3. tensorflow to run.
R_Model.R - Random forest tree created using dataset. Used to check data viability before creating model.py.
> Can be run in R Studio
Conversion_Results.xlsx - File where data was inserted into.
Conversion_Results.csv - Same as Excel Workbook but without 'formatting'. The file used by model.py and R_Model.R to download dataset.
2018RushE.csv - file containing data to be inputted into model
2019RushE.csv - see above
model.h5 (not created yet) - Saved model will be created when training is complete.

==Source==
This project could not be done without the following (both for model training and webscraping purposes). These have been instrumental for supplying model input.

https://www.espn.com/college-football/team/schedule/_/id/57/season/2018 (this link is used with the ending '/2019' as well)
https://www.teamrankings.com/college-football/stat/yards-per-pass-attempt?date=2019-12-16 (this link is used with the ending 'date=2019-12-16' as well)
https://www.sports-reference.com/cfb/years/2019-team-offense.html (this link is used with the ending '2018-team-offense.html' as well)
https://www.footballoutsiders.com/stats/ncaa/2018
https://www.espn.com/college-football/story/_/id/28251219/sp+-rankings-conference-championship-games

==Progress==

Project is still in its early stages. The data has been collected and is ready to be trained, but the model itself still needs to be built. Additionally, the functionality in the prog.py has not been implemented.