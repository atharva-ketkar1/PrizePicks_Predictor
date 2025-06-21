# PrizePicks_Predictor
Try to find the best lines in PrizePicks

## NBA Finals – 6/11/2025: OKC vs Indiana Game 3

Went 5/5 for predictions_2025-06-11.csv which used an extremely basic strategy(predict_lines.py -> predictions_2025-06-11.csv).

| Player            | Line Score | Predicted Avg | Edge  | Pick   | Results |
|-------------------|------------|----------------|--------|--------|---------|
| Pascal Siakam     | 19.5       | 26.4           | +6.9   | OVER   | ✅       |
| Chet Holmgren     | 14.5       | 18.0           | +3.5   | OVER   | ✅       |
| Aaron Nesmith     | 13.0       | 9.8            | -3.2   | UNDER  | ✅       |
| Aaron Wiggins     | 6.0        | 3.0            | -3.0   | UNDER  | ✅       |
| Andrew Nembhard   | 11.5       | 8.8            | -2.7   | UNDER  | ✅       |
 

## NBA Finals – 6/13/2025: OKC vs Indiana Game 4

### Model 1 Predictions(predict_lines.py -> predictions_2025-06-12.csv)
- Could've been 100% correct again if SGA didn't have a lot of free throws in the 4th

| Player                  | Line | Predicted | Delta | Recommendation | Result |
|-------------------------|------|-----------|--------|----------------|--------|
| Pascal Siakam           | 19.5 | 26.4      | +6.9   | OVER           | ✅     |
| Shai Gilgeous-Alexander | 34.0 | 31.4      | -2.6   | UNDER          | ❌       |

---

### Model 2 Predictions(predict_lines_v2.py -> predictions_2025-06-12_v2.csv)
- Literally got everything wrong, which is as insane as getting everything right

| Player                  | Stat | Line | Predicted | Delta | Rec   | Result |
|-------------------------|------|------|-----------|--------|--------|--------|
| Isaiah Joe              | PTS  | 2.5  | 7.8       | +5.3   | OVER   | ❌       |
| Myles Turner            | PTS  | 13.5 | 16.8      | +3.3   | OVER   | ❌       |
| Aaron Wiggins           | PTS  | 5.5  | 8.2       | +2.7   | OVER   | ❌       |
| Aaron Wiggins           | PTS  | 5.5  | 8.2       | +2.7   | OVER   | ❌       |
| Andrew Nembhard         | PTS  | 10.5 | 15.0      | +4.5   | OVER   | ❌       |
| Aaron Nesmith           | PTS  | 11.5 | 14.8      | +3.3   | OVER   | ❌       |
| Shai Gilgeous-Alexander | PTS  | 34.0 | 29.8      | -4.2   | UNDER  | ❌       |
| Isaiah Hartenstein      | PTS  | 6.0  | 9.0       | +3.0   | OVER   | ❌       |
| Tyrese Haliburton       | AST  | 8.5  | 11.6      | +3.1   | OVER   | ❌       |

---

### ML Model Predictions(nba_ml_predictions.ipynb)
- Terrible predictions

| Player                  | Team | Stat | Line | Predicted | Delta | Recommendation | Result |
|-------------------------|------|------|------|-----------|--------|----------------|--------|
| Cason Wallace           | OKC  | PTS  | 5.5  | 12.71     | +7.21  | OVER           | ❌       |
| Isaiah Joe              | OKC  | PTS  | 2.5  | 6.46      | +3.96  | OVER           | ❌       |
| Chet Holmgren           | OKC  | PTS  | 15.5 | 11.75     | -3.75  | UNDER          | ✅       |
| Isaiah Hartenstein      | OKC  | PTS  | 6.0  | 9.48      | +3.48  | OVER           | ❌       |
| Aaron Nesmith           | IND  | PTS  | 11.5 | 14.66     | +3.16  | OVER           | ❌       |
| Shai Gilgeous-Alexander | OKC  | PTS  | 34.0 | 30.86     | -3.14  | UNDER          | ❌       |


## NBA Finals – 6/16/2025: OKC vs Indiana Game 5

### Model 1 Predictions(predict_lines.py -> predictions_2025-06-15.csv)

- Another 100% success rate for Model 1

| Player                  | Line | Predicted | Delta | Recommendation | Result |
|-------------------------|------|-----------|--------|----------------|--------|
| Pascal Siakam           | 19.5 | 26.4      | +6.9   | OVER           | ✅       |
| Shai Gilgeous-Alexander | 34.5 | 31.4      | -3.1   | UNDER          | ✅       |
| Alex Caruso             | 10.5 | 7.8       | -2.7   | UNDER          | ✅       |

---

### Model 2 Predictions(predict_lines_v2.py -> predictions_2025-06-15_v2.csv)

- 4/9 correct

| Player                  | Stat | Line | Predicted | Delta | Recommendation | Result |
|-------------------------|------|------|-----------|--------|----------------|--------|
| Myles Turner            | PTS  | 14.0 | 16.8      | +2.8   | OVER           | ❌       |
| Aaron Wiggins           | PTS  | 5.0  | 8.2       | +3.2   | OVER           | ✅       |
| Andrew Nembhard         | PTS  | 10.5 | 15.0      | +4.5   | OVER           | ❌       |
| Aaron Nesmith           | PTS  | 10.5 | 14.8      | +4.3   | OVER           | ✅       |
| Isaiah Joe              | PTS  | 2.5  | 7.8       | +5.3   | OVER           | ❌       |
| Shai Gilgeous-Alexander | PTS  | 34.5 | 29.8      | -4.7   | UNDER          | ✅       |
| Isaiah Hartenstein      | PTS  | 6.0  | 9.0       | +3.0   | OVER           | ❌       |
| Obi Toppin              | REB  | 5.5  | 1.6       | -3.9   | UNDER          | ✅       |
| Tyrese Haliburton       | AST  | 8.0  | 11.6      | +3.6   | OVER           | ❌       |

## NBA Finals – 6/19/2025: OKC vs Indiana Game 6

### Model 1 Predictions(predict_lines.py -> predictions_2025-06-18.csv)

- 50%

| Player             | Line | Predicted | Delta | Recommendation | Result |
|--------------------|------|-----------|--------|----------------|--------|
| Tyrese Haliburton  | 13.5 | 19.0      | +5.5   | OVER           | ✅       |
| Pascal Siakam      | 21.0 | 26.4      | +5.4   | OVER           | ❌      |
| Aaron Wiggins      | 6.0  | 3.0       | -3.0   | UNDER          | ✅       |
| T.J. McConnell     | 10.5 | 7.6       | -2.9   | UNDER          | ❌       |

---

### Model 2 Predictions(predict_lines_v2.py -> predictions_2025-06-18_v2.csv)

- Also 50%
  
| Player                  | Stat | Line | Predicted | Delta | Recommendation | Result |
|-------------------------|------|------|-----------|--------|----------------|--------|
| Myles Turner            | PTS  | 13.5 | 16.8      | +3.3   | OVER           | ❌       |
| Andrew Nembhard         | PTS  | 10.5 | 15.0      | +4.5   | OVER           | ✅       |
| Aaron Nesmith           | PTS  | 11.0 | 14.8      | +3.8   | OVER           | ❌       |
| Tyrese Haliburton       | PTS  | 13.5 | 17.6      | +4.1   | OVER           | ✅       |
| Shai Gilgeous-Alexander | PTS  | 33.5 | 29.8      | -3.7   | UNDER          | ✅       |
| Isaiah Hartenstein      | PTS  | 5.5  | 9.0       | +3.5   | OVER           | ✅       |
| Obi Toppin              | REB  | 5.0  | 1.6       | -3.4   | UNDER          | ❌       |
| Tyrese Haliburton       | AST  | 7.0  | 11.6      | +4.6   | OVER           | ❌       |

## NBA Finals – 6/22/2025: OKC vs Indiana Game 7

### Model 1 Predictions(predict_lines.py -> predictions_2025-06-21.csv)

| Player            | Line | Predicted | Delta | Recommendation | Result |
|-------------------|------|-----------|--------|----------------|--------|
| Pascal Siakam     | 20.5 | 26.4      | +5.9   | OVER           |        |
| Aaron Wiggins     | 6.5  | 3.0       | -3.5   | UNDER          |        |
| Tyrese Haliburton | 15.5 | 19.0      | +3.5   | OVER           |        |
| Chet Holmgren     | 15.0 | 18.0      | +3.0   | OVER           |        |

---

### Model 2 Predictions(predict_lines_v2.py -> predictions_2025-06-21_v2.csv)
  
| Player                  | Stat | Line | Predicted | Delta | Recommendation | Result |
|-------------------------|------|------|-----------|--------|----------------|--------|
| Shai Gilgeous-Alexander | PTS  | 32.5 | 29.8      | -2.7   | UNDER          |        |
| Myles Turner            | PTS  | 12.0 | 16.8      | +4.8   | OVER           |        |
| Andrew Nembhard         | PTS  | 10.5 | 15.0      | +4.5   | OVER           |        |
| Aaron Nesmith           | PTS  | 10.5 | 14.8      | +4.3   | OVER           |        |
| Shai Gilgeous-Alexander | PTS  | 33.0 | 29.8      | -3.2   | UNDER          |        |
| Isaiah Hartenstein      | PTS  | 5.5  | 9.0       | +3.5   | OVER           |        |
| Chet Holmgren           | REB  | 10.0 | 7.4       | -2.6   | UNDER          |        |
| Obi Toppin              | REB  | 5.0  | 1.6       | -3.4   | UNDER          |        |
| Isaiah Hartenstein      | REB  | 6.0  | 8.8       | +2.8   | OVER           |        |
| Tyrese Haliburton       | AST  | 7.0  | 11.6      | +4.6   | OVER           |        |
