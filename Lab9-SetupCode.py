# Data set source:
# UCI Machine Learning Repository
# https://archive.ics.uci.edu/ml/datasets/Flags

# Information about the data set:
'''
Title: Flag database

Source Information
   -- Creators: Collected primarily from the "Collins Gem Guide to Flags": Collins Publishers (1986).
   -- Donor: Richard S. Forsyth 
   -- Date: 5/15/1990

Number of Instances: 194

Number of attributes: 30 (overall)

Attribute Information:
   1. name	Name of the country concerned

   2. landmass	1=N.America, 2=S.America, 3=Europe, 4=Africa, 4=Asia, 6=Oceania

   3. zone	Geographic quadrant, based on Greenwich and the Equator 1=NE, 2=SE, 3=SW, 4=NW

   4. area	in thousands of square km

   5. population	in round millions

   6. language 1=English, 2=Spanish, 3=French, 4=German, 5=Slavic, 6=Other Indo-European, 7=Chinese, 8=Arabic, 9=Japanese/Turkish/Finnish/Magyar, 10=Others

   7. religion 0=Catholic, 1=Other Christian, 2=Muslim, 3=Buddhist, 4=Hindu, 5=Ethnic, 6=Marxist, 7=Others

   8. bars     Number of vertical bars in the flag

   9. stripes  Number of horizontal stripes in the flag

  10. colours  Number of different colours in the flag

  11. red      0 if red absent, 1 if red present in the flag
  12. green    same for green
  13. blue     same for blue
  14. gold     same for gold (also yellow)
  15. white    same for white
  16. black    same for black
  17. orange   same for orange (also brown)

  18. mainhue  predominant colour in the flag (tie-breaks decided by taking the topmost hue, if that fails then the most central hue, and if that fails the leftmost hue)

  19. circles  Number of circles in the flag
  20. crosses  Number of (upright) crosses
  21. saltires Number of diagonal crosses
  22. quarters Number of quartered sections
  23. sunstars Number of sun or star symbols

  24. crescent 1 if a crescent moon symbol present, else 0
  25. triangle 1 if any triangles present, 0 otherwise
  26. icon     1 if an inanimate image present (e.g., a boat), otherwise 0
  27. animate  1 if an animate image (e.g., an eagle, a tree, a human hand) present, 0 otherwise
  28. text     1 if any letters or writing on the flag (e.g., a motto or slogan), 0 otherwise

  29. topleft  colour in the top-left corner (moving right to decide  tie-breaks)

  30. botright Colour in the bottom-left corner (moving left to decide tie-breaks)
'''





import pandas
import sqlite3

def extract(filename,dbname):
    '''
    Opens the file with filename and extracts to a database dbname
    '''
    names = ["name","landmass","zone","area","population",
                "language","religion","bars","stripes","colours", "red","green","blue",
                "gold","white","black","orange","mainhue","circles","crosses","saltires","quarters",
                "sunstars","crescent","triangle","icon","animate","text","topleft","botright"]
    flag = pandas.read_csv(filename,names=names)

    conn=sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("DROP table IF EXISTS flag") # Get rid of the table if it already exists
    sql = '''CREATE TABLE flag (name text, landmass int, zone int, area int, population int, language int, 
                                religion int, bars int, stripes int, colours int,
                                red bool, green bool, blue bool, gold bool, white bool, black bool, orange bool,
                                mainhue text, circles int, crosses int, saltires int, quarters int, sunstars int,
                                crescent bool, triangle bool, icon bool, animate bool, text bool, topleft text, botright text)'''
    cur.execute(sql)
    
    for i in range(len(flag)):
        attributes = []
        for column in names:
            entry = flag[column][i]
            if type(entry) == str:
                entry = "'" + entry + "'"
            else:
                entry = int(entry)
            attributes.append(entry)
        sql = "INSERT INTO flag VALUES (%s)" % attributes
        sql = sql.replace("[","").replace("]","").replace("\"","")
        cur.execute(sql)
        
    conn.commit()
    conn.close()
    
def showallflagdata():
    flagquery("SELECT * FROM flag")
    
def flagquery(sql):
    '''
    INPUT: A string to be used as a SQL query.
    OUTPUT: prints result of given query. Commits query to database.
    '''
    conn=sqlite3.connect('flag.db')
    cur=conn.cursor()
    result = cur.execute(sql)
    for i in result:
        print(i)
    conn.commit()
    conn.close()
    

extract("flag.csv","flag.db")




#showallflagdata()
# flagquery("UPDATE flag SET population = 328 WHERE name == 'USA'") # Updates the population of the USA to present-day numbers
# flagquery("SELECT * FROM flag WHERE sunstars == 50") (Finds all countries with 50 stars [or suns] on their flag)
#flagquery("SELECT name FROM flag WHERE landmass == 2") # Finds the names of all countries in South America
#flagquery("ALTER TABLE flag DROP COLUMN circles") # Deletes the circles column





