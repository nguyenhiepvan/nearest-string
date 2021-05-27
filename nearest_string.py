import numpy as np
from itertools import combinations
import re,sys

def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return "The strings are {} edits away".format(distance[row][col])

s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
def remove_accents(input_str):
    s = ''
    for c in input_str:
        if c in s1:
            s += s0[s1.index(c)]
        else:
            s += c
    return s

def optimize(title):
  exts = ['.docx','.doc', '.pdf', '.pptx', '.ppt','.potx',  '.pot','.ppsx' '.pps' ]
  title = title.replace(" ", "").upper()
  for ext in exts:
    title = title.replace(ext.upper(),"")
  title = re.sub(r"[-_()\"#/@;:<>{}`+=~|.!?,]", "", title)
  return remove_accents(title)


def getMaxScore(data,title):
 scores = []
 for item in data:
  item = optimize(item)
  score = levenshtein_ratio_and_distance(title,item,True)
  scores.append(score)
 max_value = max(scores)   

 for index, item in enumerate(scores, start=1):
  if item == max_value:
      max_key = index
      break

 for index, item in enumerate(data, start=1):
  if index == max_key:
      results = item

 return [max_value,' '.join(results.split())]

def clean_head(title,results):
 start = title[0:10]
 tmp_result = results
 
 while len(tmp_result) > 0:
  tmp = optimize(tmp_result)
  tmp = remove_accents(tmp)
  if start == tmp[0:10]:
      break
  tmp_result = tmp_result[1::]

 if len(tmp_result) > 0:
     return re.sub(r"[-_()\"#/@;:<>{}`+=~|.!?,]", "", tmp_result).upper()

 return re.sub(r"[-_()\"#/@;:<>{}`+=~|.!?,]", "", results).upper()

def clean_tail(title,results):
 end = title[len(title)-5:len(title)]
 tmp_result = results
 
 while len(tmp_result) > 0:
  tmp = optimize(tmp_result)
  tmp = remove_accents(tmp)
  if end == tmp[len(tmp)-10:len(tmp)]:
      break
  tmp_result = tmp_result[:-1:]

 if len(tmp_result) > 0:
     return re.sub(r"[-_()\"#/@;:<>{}`+=~|.!?,]", "", tmp_result).upper()

 return re.sub(r"[-_()\"#/@;:<>{}`+=~|.!?,]", "", results).upper()

def clean(title,results):
    results = clean_head(title,results)
    return clean_tail(title,results)

def optimizeResult(results,title,max_value):
 terms = results.split(" ")

 for index, item in enumerate(terms, start=1):
    tmp = results
    tmp = re.sub(' +', ' ',tmp.replace(item,"",1))
    new_score = levenshtein_ratio_and_distance(optimize(item),title,True)
    if new_score >= max_value:
        results = tmp
        max_value = new_score

 return clean(title,results)


def getBestMatch(title,text):
 original = title
 title = optimize(title)
 terms = text.split(" ")
 data = []
 tmp = ""
 for i in range(len(terms) - 1):
    tmp += " " + terms[i]
    for j in range(i+1,len(terms)):
        tmp = tmp + " " + terms[j]
        if len(tmp) > 1.5 * len(original):
         data.append(tmp)
         tmp = ""
         break

 [max_value,results] = getMaxScore(data,title)
 if max_value < 0.5:
     return re.sub(r"[-_()\"#/@;:<>{}`+=~|.!?,]", " ", original).upper()
 
 return optimizeResult(results,title,max_value)

def main():
 args = sys.argv[1:]
 print(getBestMatch(args[0],args[1]))