Edit: The formatting is better when run with cat in terminal.

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

The data collected is below. However, some of these were found to be redundant and will not be included in the final model (see R_Model.R for more details).
Column					Description						Feature Type	Data Type	Included
Down					3rd or 4th Down						Categorical	Integer		Yes
Score Differential			Florida Score - Opponent Score				Numerical	Integer		Yes
Current Quarter				Quarter the game is in (1,2,3,4)			Categorical	Integer		Yes
Opponent Offense 			Offense SP+ at end of season				Numerical	Double		No
Opponent Offense Rank			Offense SP+ Rank Among FBS Teams			Numerical	Integer		Yes
Rush Efficiency				Opponent Yards Per Rush					Numerical	Double		No
Rush Rank				Opponent Yards Per Rush Rank Among FBS Teams		Numerical	Integer		Yes
Pass Efficiency				Opponent Yards Per Pass Atempt				Numerical	Double		No
Pass Rank				Opponent Yards Per Pass Atempt Rank Among FBS Teams	Numerical	Integer		Yes
Rush Grade				Opponent Offense SP+ Rank + Yards Per Rush		Numerical	Integer		No
Pass Grade				Opponent Offense SP+ Rank + Yards Per Pass Attempt	Numerical	Integer		No
Opponent Play				Run or Pass						Categorical	String		Yes
Yards-To-Go				3rd-and-?						Numerical	Integer		Yes
Yards-To-Goal				# of yards away from touchdown				Numerical	Integer		Yes
Number of Yards Gained			Likely won't be utilized				Numerical	Integer		No
Location				Away, Neutral, Home					Categorical	String		Yes
Result					Conversion,Non-Conversion,Sack,Interception,Fumble	Categorical	String		Yes

==Important Files Contained in Repository==

WARNING: TensorFlow and its features may prove difficult to install properly. This may or may not take several hours to install properly. I found that Protobuf needed be installed as version 3.6.0 for the code to compile properly. I have found TensorFlow 2.0.0 to work best too. The Python code was written in version 3.6.0. Using an older version (particularly below 3.0.0 would cause problems in compiling the code). This code has only been tested in Windows and I cannot gurantee that it would work in a different OS. 

prog.py - File where the model can be interacted with. Only file that needs to be run.
  python prog.py
model.py - File where model is to be created and trained.
> python model.py
> requires 1. numpy, 2. pandas, 3. tensorflow 4. keras 5. sklearn among other libraries to run.
storage.py - File that stores a few pre-defined lists. It is incorporated by prog.py and is not necessary to understand.
R_Model.R - Random forest tree created using dataset. Used to check data viability before creating model.py.
  Can be run in R Studio
Conversion_Results.xlsx - File where data was inserted into.
Conversion_Results.csv - Same as Excel Workbook but without 'formatting'. The file used by model.py and R_Model.R to download dataset.
2018RushE.csv - file containing data to be inputted into model
2019RushE.csv - see above
model.h5 (not created yet) - Saved model will be created when training is complete.

==Sources==
This project could not be done without the following (both for model training and webscraping purposes). These have been instrumental for supplying model input.

https://www.espn.com/college-football/team/schedule/_/id/57/season/2018 (this link is used with the ending '/2019' as well)

https://www.teamrankings.com/college-football/stat/yards-per-pass-attempt?date=2019-12-16 (this link is used with the ending 'date=2019-12-16' as well)

https://www.sports-reference.com/cfb/years/2019-team-offense.html (this link is used with the ending '2018-team-offense.html' as well)

https://www.footballoutsiders.com/stats/ncaa/2018

https://www.espn.com/college-football/story/_/id/28497018/final-sp+-rankings-2019-college-football-season

==Progress==

The data has been collected and is ready to be trained. The model itself is close to completion but is not ready to be trained at this time. Additionally, the functionality in the prog.py has not been implemented.
