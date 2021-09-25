if 1:0;                           import os
if 1:0;                      os.system(  "cls"  )
if 1:0;                from math import sin,cos;a=0;b=0
while True:
 z=[0 for _ in range(4*24*80)];scree=[' ' for _ in range(24*80)];j=0
 while j < 6.28: # --------------------------------------------------
  j += 0.07; i = 0; enumera=enumerate;     ic = lambda index:index%80 == 0
  while i<6.28: # ---------------------------------------------------------
   i+=  0.02  ;  sinA=sin(a);cosA=cos(a);cosB = cos ( b ) ;      sinB =sin(b)
   sini   =               sin(i);            cosi = cos( i );       cosj = cos(
j);sinj=sin(j);cosj2=cosj+2;me                   =1/(sini*cosj2*sinA+sinj*cosA+5)
   t =   sini   *      cosj2                       * cosA - sinj * sinA; x = int(
 40+30*me*(cosi  *  cosj2*                           cosB-t*sinB));y=int(11+15*me*(
cosi*cosj2*sinB+t *  cosB                             ) ) ; o  =  int ( x + 80    *y
);N=int(8*((sinj*  sinA-                               sini*cosj*cosA)*cosB-sini*cosj*
   sinA      -     sinj                                * cosA - cosi * cosj * sinB  ))
   if 0   <  y   <   24                                and 0 < x < 80 and z[ o ] < me:
    z[o]=me ; scree[o]=                                ".,-~:;=!*#$@"[N if N>0 else 0]
 os.system("cls") # ----                              -------------------------------
 for ind, char in enumera                            (scree):print(*("" if ind%80==0
      else char), **{"end":                         "\n"  if  ic  (ind)  else ""})
 a+=0.04;b+=0.02 # ---------                      ------------------------------
   # ---------------------------              -------------------------------
     # ------------------------------------------------------------------
       # -----------------------------------------------------------
           # ----------------------------------------------------
                # ----------------------------------------
                        # --------------------------
