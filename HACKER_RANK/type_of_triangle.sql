select case when ((A+B)<= C or (B+C)<=A or (C+A)<=B) THEN 'Not A Triangle'
            when ((A=B) AND (B=C)) THEN 'Equilateral'
            when (A=B) OR (B=C) OR (C=A) THEN 'Isosceles'
            else 'Scalene' end  
from TRIANGLES