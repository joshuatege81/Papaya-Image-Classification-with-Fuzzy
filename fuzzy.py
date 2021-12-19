import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl #package fuzzy utk implemetasi macam tools pada proses fuzzy
# import anvil.server
import matplotlib.pyplot as plt
import pandas as pd

# contoh = ctrl.Antecedent(np.arange(batas_bawah,batas_atas,jarak_antara), 'namanya_apa')
# ingat yahh koma tuh titik dsinii
# jarak_antara sekarang ini diisi sma batas_bawah + batas_atas dibagi banyaknya membership
def fuzzy():
    energy0 = ctrl.Antecedent(np.arange(0.173958, 0.635533, 0.153858), 'Energy0')
    homogeneity0 = ctrl.Antecedent(np.arange(0.527904, 0.836820, 0.102971), 'Homogeneity0')  # jarak sebenarnya 0.102971
    entropy0 = ctrl.Antecedent(np.arange(2.011137, 5.233180, 1.074014), 'Entropy0')
    contrast0 = ctrl.Antecedent(np.arange(116.378568, 338.184670, 73.935367), 'Contrast0')

    energy45 = ctrl.Antecedent(np.arange(0.165705, 0.628945, 0.154413), 'Energy45')
    homogeneity45 = ctrl.Antecedent(np.arange(0.500059, 0.825861, 0.108600), 'Homogeneity45')  # jarak sebenarnya 0.108601
    entropy45 = ctrl.Antecedent(np.arange(2.088229, 5.377328, 1.096366), 'Entropy45')
    contrast45 = ctrl.Antecedent(np.arange(234.516089, 570.949036, 112.144315), 'Contrast45')

    energy90 = ctrl.Antecedent(np.arange(0.171264, 0.634649, 0.154461), 'Energy90')
    homogeneity90 = ctrl.Antecedent(np.arange(0.515930, 0.834426, 0.106165), 'Homogeneity90')
    entropy90 = ctrl.Antecedent(np.arange(2.025571, 5.259427, 1.077951), 'Entropy90')  # jarak sebenarnya 1.077952
    contrast90 = ctrl.Antecedent(np.arange(121.707431, 461.934424, 113.408997), 'Contrast90')

    energy135 = ctrl.Antecedent(np.arange(0.165182, 0.629635, 0.154817), 'Energy135')
    homogeneity135 = ctrl.Antecedent(np.arange(0.499191, 0.826905, 0.109237), 'Homogeneity135')  # jarak sebenarnya 0.109238
    entropy135 = ctrl.Antecedent(np.arange(2.078079, 5.403592, 1.108504), 'Entropy135')
    contrast135 = ctrl.Antecedent(np.arange(226.559489, 578.083018, 117.174509), 'Contrast135')

    result = ctrl.Consequent(np.arange(0, 5, 1), 'result')

    #==============================================DERAJAT O================================================================
        # namanya['kategori_brpa'] = fuzz.trimf(namanya.universe,[batas_bawah, nilai_tertinggi, batas_atas])
        # ingat yahh koma tuh titik dsinii
    energy0['1'] = fuzz.trimf(energy0.universe,[ 0.020100, 0.173958, 0.327816])
    energy0['2'] = fuzz.trimf(energy0.universe,[ 0.173958, 0.327816, 0.481674])
    energy0['3'] = fuzz.trimf(energy0.universe,[ 0.327816, 0.481674, 0.635532])
    energy0['4'] = fuzz.trimf(energy0.universe,[ 0.481674, 0.635532, 0.78939])
    #energy0.view()

    homogeneity0['1'] = fuzz.trimf(homogeneity0.universe,[0.424932, 0.527904, 0.630876])
    homogeneity0['2'] = fuzz.trimf(homogeneity0.universe,[0.527904, 0.630876, 0.733848])
    homogeneity0['3'] = fuzz.trimf(homogeneity0.universe,[0.630876, 0.733848, 0.836820])
    homogeneity0['4'] = fuzz.trimf(homogeneity0.universe,[0.733848, 0.836820, 0.939792])
    #homogeneity0.view()

    entropy0['1'] = fuzz.trimf(entropy0.universe,[0.937123, 2.011137, 3.085151])
    entropy0['2'] = fuzz.trimf(entropy0.universe,[2.011137, 3.085151, 4.159165])
    entropy0['3'] = fuzz.trimf(entropy0.universe,[3.085151, 4.159165, 5.233179])
    entropy0['4'] = fuzz.trimf(entropy0.universe,[4.159165,5.233179, 6.307193])
    #entropy0.view()

    contrast0['1'] = fuzz.trimf(contrast0.universe,[42.443201, 116.378568, 190.313858])
    contrast0['2'] = fuzz.trimf(contrast0.universe,[116.378568, 190.313858, 264.249302])
    contrast0['3'] = fuzz.trimf(contrast0.universe,[190.313858, 264.249302, 338.184669])
    contrast0['4'] = fuzz.trimf(contrast0.universe,[264.249302, 338.184669, 412.120036])
    #contrast0.view()


    #=========================================DERAJAT 45====================================================================
    # namanya['kategori_brpa'] = fuzz.trimf(namanya.universe,[batas_bawah, nilai_tertinggi, batas_atas])
    # ingat yahh koma tuh titik dsinii
    energy45['1'] = fuzz.trimf(energy45.universe,[0.011292, 0.165705, 0.320118])
    energy45['2'] = fuzz.trimf(energy45.universe, [0.165705, 0.320118, 0.474531])
    energy45['3'] = fuzz.trimf(energy45.universe,[ 0.320118, 0.474531, 0.628944])
    energy45['4'] = fuzz.trimf(energy45.universe,[ 0.474531, 0.628944, 0.783357])
    #energy45.view()

    homogeneity45['1'] = fuzz.trimf(homogeneity45.universe,[0.391458, 0.500059, 0.608659])
    homogeneity45['2'] = fuzz.trimf(homogeneity45.universe,[0.500059, 0.608659, 0.717259])
    homogeneity45['3'] = fuzz.trimf(homogeneity45.universe,[0.608659, 0.717259, 0.825859])
    homogeneity45['4'] = fuzz.trimf(homogeneity45.universe,[0.717259, 0.825859, 0.934460])
    #homogeneity45.view()

    entropy45['1'] = fuzz.trimf(entropy45.universe,[0.991863, 2.088229, 3.184595])
    entropy45['2'] = fuzz.trimf(entropy45.universe,[2.088229, 3.184595, 4.280961])
    entropy45['3'] = fuzz.trimf(entropy45.universe,[3.184595, 4.280961, 5.377327])
    entropy45['4'] = fuzz.trimf(entropy45.universe,[4.280961,5.377327, 6.473693])
    #entropy45.view()

    contrast45['1'] = fuzz.trimf(contrast45.universe,[122.371774, 234.516089, 346.660404])
    contrast45['2'] = fuzz.trimf(contrast45.universe,[234.516089, 346.660404, 458.804719])
    contrast45['3'] = fuzz.trimf(contrast45.universe,[346.660404, 458.804719, 570.949034])
    contrast45['4'] = fuzz.trimf(contrast45.universe,[458.804719,570.949034, 683.093349])
    #contrast45.view()



    #===========================================DERAJAT 90==================================================================
        # namanya['kategori_brpa'] = fuzz.trimf(namanya.universe,[batas_bawah, nilai_tertinggi, batas_atas])
        # ingat yahh koma tuh titik dsinii

    energy90['1'] = fuzz.trimf(energy90.universe,[0.016803, 0.171264, 0.325725])
    energy90['2'] = fuzz.trimf(energy90.universe,[0.171264, 0.325725, 0.480186])
    energy90['3'] = fuzz.trimf(energy90.universe,[0.325725, 0.480186, 0.634647])
    energy90['4'] = fuzz.trimf(energy90.universe,[0.480186, 0.634647, 0.789108])
    #energy90.view()

    homogeneity90['1'] = fuzz.trimf(homogeneity90.universe,[0.409765, 0.515930, 0.622095])
    homogeneity90['2'] = fuzz.trimf(homogeneity90.universe,[0.515930, 0.622095, 0.72826])
    homogeneity90['3'] = fuzz.trimf(homogeneity90.universe,[0.622095, 0.72826, 0.834425])
    homogeneity90['4'] = fuzz.trimf(homogeneity90.universe,[0.72826, 0.834425, 0.94059])
    #homogeneity90.view()

    entropy90['1'] = fuzz.trimf(entropy90.universe,[0.947619, 2.025571, 3.103523])
    entropy90['2'] = fuzz.trimf(entropy90.universe,[2.025571, 3.103523, 4.181475])
    entropy90['3'] = fuzz.trimf(entropy90.universe,[3.103523, 4.181475, 5.259427])
    entropy90['4'] = fuzz.trimf(entropy90.universe,[4.181475, 5.259427, 6.337379])
    #entropy90.view()

    contrast90['1'] = fuzz.trimf(contrast90.universe,[8.298434, 121.707431, 235.116428])
    contrast90['2'] = fuzz.trimf(contrast90.universe,[121.707431, 235.116428, 348.525425])
    contrast90['3'] = fuzz.trimf(contrast90.universe,[ 235.116428,348.525425, 461.934422 ])
    contrast90['4'] = fuzz.trimf(contrast90.universe,[348.525425,461.934422, 575.343419])
    #contrast90.view()


    #===============================================DERAJAT 135=============================================================
        # namanya['kategori_brpa'] = fuzz.trimf(namanya.universe,[batas_bawah, nilai_tertinggi, batas_atas])
        # ingat yahh koma tuh titik dsinii
    energy135['1'] = fuzz.trimf(energy135.universe,[0.010365 ,0.165182 , 0.319999])
    energy135['2'] = fuzz.trimf(energy135.universe,[0.165182 ,0.319999, 0.474816])
    energy135['3'] = fuzz.trimf(energy135.universe,[0.319999, 0.474816, 0.629633])
    energy135['4'] = fuzz.trimf(energy135.universe,[0.474816, 0.629633, 0.78445])
    #energy135.view()

    homogeneity135['1'] = fuzz.trimf(homogeneity135.universe,[0.389953, 0.499191, 0.608429])
    homogeneity135['2'] = fuzz.trimf(homogeneity135.universe,[0.499191, 0.608429, 0.717667])
    homogeneity135['3'] = fuzz.trimf(homogeneity135.universe,[0.608429, 0.717667, 0.826905])
    homogeneity135['4'] = fuzz.trimf(homogeneity135.universe,[0.717667, 0.826905, 0.936143])
    #homogeneity135.view()

    entropy135['1'] = fuzz.trimf(entropy135.universe,[0.969575, 2.078079, 3.186583])
    entropy135['2'] = fuzz.trimf(entropy135.universe,[2.078079, 3.186583, 4.295087])
    entropy135['3'] = fuzz.trimf(entropy135.universe,[3.186583, 4.295087, 5.403591])
    entropy135['4'] = fuzz.trimf(entropy135.universe,[4.295087, 5.403591, 6.512095])
    #entropy135.view()

    contrast135['1'] = fuzz.trimf(contrast135.universe,[109.384980, 226.559489, 343.733998])
    contrast135['2'] = fuzz.trimf(contrast135.universe,[226.559489, 343.733998, 460.908507])
    contrast135['3'] = fuzz.trimf(contrast135.universe,[343.733998, 460.908507,578.083016])
    contrast135['4'] = fuzz.trimf(contrast135.universe,[460.908507,578.083016, 695.257525])
    #contrast135.view()

    #=======================KATEGORI KEMATANGAN=================================================

    #namanya['kategori_brpa'] = fuzz.trimf(namanya.universe,[batas_bawah, nilai_tertinggi, batas_atas])
    # ingat yahh koma tuh titik dsinii
    result['mentah'] = fuzz.trimf(result.universe, [0, 1, 2])
    result['setengah_matang'] = fuzz.trimf(result.universe, [1, 2, 3])
    result['matang'] = fuzz.trimf(result.universe, [2, 3, 4])

    #result.view()

    #==============================================RULES====================================================================
    rl1 = ctrl.Rule(energy0['4'] & homogeneity0['4'] & entropy0['1'] & contrast0['1']
                    & energy45['4'] & homogeneity45['4'] & entropy45['1'] & contrast45['1']
                    & energy90['4'] & homogeneity90['4'] & entropy90['1'] & contrast90['1']
                    & energy135['4'] & homogeneity135['4'] & entropy135['1'] & contrast135['1'], result['mentah'])#p1

    rl2 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['1']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['1']
                & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['1']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['1'], result['mentah'])#p2

    rl3 = ctrl.Rule(energy0['2'] & homogeneity0['3'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['2']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['mentah'])#p3

    rl4 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['2']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['setengah_matang'])#p4

    rl5 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['2']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['setengah_matang'])#p5

    rl6 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['2']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['2']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['2'], result['setengah_matang'])#p6 cek lg

    rl7 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['1'] & contrast0['2']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['2']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['2'], result['setengah_matang'])#p7

    rl8 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['2']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['3']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['2'], result['matang'])#p8

    rl9 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['1']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['1']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['2']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['2'], result['matang'])#p9

    rl10 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['1']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['1']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['setengah_matang'])#p13

    rl11 = ctrl.Rule(energy0['2'] & homogeneity0['3'] & entropy0['3'] & contrast0['1']
                    & energy45['2'] & homogeneity45['3'] & entropy45['3'] & contrast45['1']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['setengah_matang'])#p14

    rl12 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['2']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['1']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['1'], result['matang'])#p15

    rl13 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['1']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['3']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['2'], result['matang'])#p17

    rl14 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['1']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['3']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['3'], result['matang'])#p18

    rl15 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['1']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['3']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['2'], result['matang'])#p20

    rl16 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['1']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['1']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['mentah'])#p21

    rl17 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['1']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['1']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['1'], result['setengah_matang'])#p22

    rl18 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['1']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['1']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['setengah_matang'])#p23

    rl19 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['2']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['setengah_matang'])#p24

    rl20= ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['2']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['1']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['3']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['3'], result['mentah'])#p25

    rl21 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['1']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['1']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['2'] & contrast135['2'], result['mentah'])#p26


    rl22 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['1']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['2']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['mentah'])#p27

    rl23 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['2']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['mentah'])#p28

    rl24 = ctrl.Rule(energy0['2'] & homogeneity0['3'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['3'] & entropy45['3'] & contrast45['3']
                    & energy90['2'] & homogeneity90['3'] & entropy90['3'] & contrast90['4']
                    & energy135['2'] & homogeneity135['3'] & entropy135['3'] & contrast135['3'], result['setengah_matang'])#p30

    rl25 = ctrl.Rule(energy0['2'] & homogeneity0['3'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['3'] & entropy45['3'] & contrast45['1']
                    & energy90['2'] & homogeneity90['3'] & entropy90['3'] & contrast90['3']
                    & energy135['2'] & homogeneity135['3'] & entropy135['3'] & contrast135['3'], result['setengah_matang'])#p31

    rl26 = ctrl.Rule(energy0['4'] & homogeneity0['4'] & entropy0['1'] & contrast0['2']
                    & energy45['4'] & homogeneity45['4'] & entropy45['1'] & contrast45['2']
                    & energy90['4'] & homogeneity90['4'] & entropy90['1'] & contrast90['2']
                    & energy135['4'] & homogeneity135['4'] & entropy135['1'] & contrast135['2'], result['mentah'])#p32

    rl27 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['3']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['3'], result['matang'])#p33

    rl28 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['3']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['3']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['4'], result['matang'])#p34

    rl29 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['3']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['3']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['3'], result['matang'])#p35

    rl30 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['1']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['1']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['1'], result['setengah_matang'])#p36

    rl31 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['2']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['1']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['setengah_matang'])#p37

    rl32 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['2']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['matang'])#p38

    rl33 = ctrl.Rule(energy0['1'] & homogeneity0['2'] & entropy0['4'] & contrast0['2']
                    & energy45['1'] & homogeneity45['2'] & entropy45['4'] & contrast45['2']
                    & energy90['1'] & homogeneity90['2'] & entropy90['4'] & contrast90['2']
                    & energy135['1'] & homogeneity135['2'] & entropy135['4'] & contrast135['2'], result['mentah'])#p41

    rl34 = ctrl.Rule(energy0['1'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['1'] & homogeneity45['2'] & entropy45['3'] & contrast45['2']
                    & energy90['1'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['1'] & homogeneity135['2'] & entropy135['3'] & contrast135['1'], result['mentah'])#p42

    rl35 = ctrl.Rule(energy0['4'] & homogeneity0['4'] & entropy0['1'] & contrast0['2']
                    & energy45['4'] & homogeneity45['4'] & entropy45['1'] & contrast45['1']
                    & energy90['4'] & homogeneity90['4'] & entropy90['1'] & contrast90['2']
                    & energy135['4'] & homogeneity135['4'] & entropy135['1'] & contrast135['1'], result['mentah'])#p43

    rl36 = ctrl.Rule(energy0['4'] & homogeneity0['4'] & entropy0['1'] & contrast0['2']
                    & energy45['4'] & homogeneity45['4'] & entropy45['1'] & contrast45['1']
                    & energy90['4'] & homogeneity90['4'] & entropy90['1'] & contrast90['1']
                    & energy135['4'] & homogeneity135['4'] & entropy135['1'] & contrast135['2'], result['mentah'])#p44

    rl37 = ctrl.Rule(energy0['1'] & homogeneity0['1'] & entropy0['4'] & contrast0['3']
                    & energy45['1'] & homogeneity45['2'] & entropy45['4'] & contrast45['1']
                    & energy90['1'] & homogeneity90['1'] & entropy90['4'] & contrast90['2']
                    & energy135['1'] & homogeneity135['1'] & entropy135['4'] & contrast135['3'], result['mentah'])#p45

    rl38 = ctrl.Rule(energy0['3'] & homogeneity0['4'] & entropy0['1'] & contrast0['2']
                    & energy45['4'] & homogeneity45['4'] & entropy45['1'] & contrast45['3']
                    & energy90['4'] & homogeneity90['4'] & entropy90['1'] & contrast90['1']
                    & energy135['3'] & homogeneity135['4'] & entropy135['1'] & contrast135['3'], result['mentah'])#p46

    rl39 = ctrl.Rule(energy0['3'] & homogeneity0['4'] & entropy0['2'] & contrast0['2']
                    & energy45['3'] & homogeneity45['4'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['4'] & entropy90['2'] & contrast90['3']
                    & energy135['3'] & homogeneity135['4'] & entropy135['2'] & contrast135['3'], result['mentah'])#p48

    rl40 = ctrl.Rule(energy0['3'] & homogeneity0['4'] & entropy0['2'] & contrast0['2']
                    & energy45['3'] & homogeneity45['4'] & entropy45['2'] & contrast45['2']
                    & energy90['4'] & homogeneity90['4'] & entropy90['2'] & contrast90['2']
                    & energy135['3'] & homogeneity135['4'] & entropy135['2'] & contrast135['2'], result['mentah'])#p49

    rl41 = ctrl.Rule(energy0['3'] & homogeneity0['4'] & entropy0['1'] & contrast0['2']
                    & energy45['3'] & homogeneity45['4'] & entropy45['1'] & contrast45['2']
                    & energy90['3'] & homogeneity90['4'] & entropy90['1'] & contrast90['2']
                    & energy135['4'] & homogeneity135['4'] & entropy135['2'] & contrast135['2'], result['mentah'])#p50

    rl42 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['3']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['4']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['3']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['3'], result['mentah'])#p51

    rl43 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['2']
                    & energy45['2'] & homogeneity45['3'] & entropy45['2'] & contrast45['3']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['3']
                    & energy135['2'] & homogeneity135['3'] & entropy135['2'] & contrast135['3'], result['setengah_matang'])#p52

    rl44 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['3']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['3']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['3'], result['setengah_matang'])#p53

    rl45 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['3']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['3']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['3'], result['setengah_matang'])#p54

    rl46 = ctrl.Rule(energy0['2'] & homogeneity0['3'] & entropy0['3'] & contrast0['1']
                    & energy45['2'] & homogeneity45['3'] & entropy45['1'] & contrast45['2']
                    & energy90['2'] & homogeneity90['3'] & entropy90['3'] & contrast90['3']
                    & energy135['2'] & homogeneity135['3'] & entropy135['3'] & contrast135['3'], result['setengah_matang'])#p55


    rl47 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['1']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['1']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['mentah'])#p56


    rl48 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['1']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['1']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['1']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['setengah_matang'])#p57


    rl49 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['3']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['2']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['1']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['setengah_matang'])#p58


    rl50 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['2']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['1']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['setengah_matang'])#p59


    rl51 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['2']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['2']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['2'], result['mentah'])#p60


    rl52 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['1']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['1']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['mentah'])#p61


    rl53 = ctrl.Rule(energy0['1'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['1'] & homogeneity45['2'] & entropy45['3'] & contrast45['1']
                    & energy90['1'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['1'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['mentah'])#p62


    rl54 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['4']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['3']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['mentah'])#p63


    rl55 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['1']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['1']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['mentah'])#p64


    rl56 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['3']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['setengah_matang'])#p65


    rl57 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['3']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['4']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['4']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['4'], result['matang'])#p66


    rl58 = ctrl.Rule(energy0['3'] & homogeneity0['4'] & entropy0['1'] & contrast0['2']
                    & energy45['3'] & homogeneity45['4'] & entropy45['1'] & contrast45['2']
                    & energy90['3'] & homogeneity90['4'] & entropy90['1'] & contrast90['2']
                    & energy135['3'] & homogeneity135['4'] & entropy135['1'] & contrast135['2'], result['mentah'])#p67


    rl59 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['2']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['3']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['3'], result['mentah'])#p68


    rl60 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['3']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['4']
                    & energy135['2'] & homogeneity135['2'] & entropy135['2'] & contrast135['3'], result['matang'])#p69


    rl61 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['3']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['4']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['4']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['4'], result['matang'])#p70


    rl62 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['3']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['3']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['3']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['2'], result['setengah_matang'])#p71



    rl63 = ctrl.Rule(energy0['2'] & homogeneity0['2'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['2'] & entropy45['3'] & contrast45['4']
                    & energy90['2'] & homogeneity90['2'] & entropy90['3'] & contrast90['3']
                    & energy135['2'] & homogeneity135['2'] & entropy135['3'] & contrast135['3'], result['setengah_matang'])#p72


    rl64 = ctrl.Rule(energy0['1'] & homogeneity0['1'] & entropy0['4'] & contrast0['2']
                    & energy45['1'] & homogeneity45['1'] & entropy45['4'] & contrast45['2']
                    & energy90['1'] & homogeneity90['1'] & entropy90['4'] & contrast90['2']
                    & energy135['1'] & homogeneity135['1'] & entropy135['4'] & contrast135['2'], result['mentah'])#p74


    rl65 = ctrl.Rule(energy0['1'] & homogeneity0['1'] & entropy0['4'] & contrast0['4']
                    & energy45['1'] & homogeneity45['2'] & entropy45['4'] & contrast45['2']
                    & energy90['1'] & homogeneity90['1'] & entropy90['4'] & contrast90['2']
                    & energy135['1'] & homogeneity135['1'] & entropy135['4'] & contrast135['2'], result['mentah'])#p75

    rl66 = ctrl.Rule(energy0['1'] & homogeneity0['1'] & entropy0['4'] & contrast0['2']
                    & energy45['1'] & homogeneity45['1'] & entropy45['4'] & contrast45['2']
                    & energy90['1'] & homogeneity90['1'] & entropy90['4'] & contrast90['2']
                    & energy135['1'] & homogeneity135['1'] & entropy135['4'] & contrast135['2'], result['mentah'])#p76

    rl67 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['2']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['2']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['2'], result['mentah'])#p77

    rl68 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['2']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['2']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['3'], result['mentah'])#p78

    rl69 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['3']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['2']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['2'], result['mentah'])#p79


    rl70 = ctrl.Rule(energy0['3'] & homogeneity0['4'] & entropy0['2'] & contrast0['2']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['2']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['2'], result['mentah'])#p80

    rl71 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['2']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['3']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['2']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['2'], result['mentah'])#p81

    rl72 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['2']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['3']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['2']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['2'], result['mentah'])#p82

    rl73 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['3']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['2']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['3'], result['mentah'])#p83

    rl74 = ctrl.Rule(energy0['3'] & homogeneity0['3'] & entropy0['2'] & contrast0['2']
                    & energy45['3'] & homogeneity45['3'] & entropy45['2'] & contrast45['2']
                    & energy90['3'] & homogeneity90['3'] & entropy90['2'] & contrast90['3']
                    & energy135['3'] & homogeneity135['3'] & entropy135['2'] & contrast135['3'], result['mentah'])#p84

    rl75 = ctrl.Rule(energy0['2'] & homogeneity0['3'] & entropy0['3'] & contrast0['2']
                    & energy45['2'] & homogeneity45['3'] & entropy45['3'] & contrast45['2']
                    & energy90['2'] & homogeneity90['3'] & entropy90['3'] & contrast90['2']
                    & energy135['2'] & homogeneity135['3'] & entropy135['3'] & contrast135['2'], result['mentah'])#p85

        # for i in range(1,81):
        #     print("rl" + str(i), end=",")

    #============= RESULTING RULES===================
    resulting_ctrl = ctrl.ControlSystem([rl1,rl2,rl3,rl4,rl5,rl6,rl7,rl8,rl9,rl10,rl11,rl12,rl13,rl14,rl15,rl16,rl17,rl18,rl19,rl20,rl21,rl22,rl23,rl24,rl25,rl26,rl27,rl28,rl29,rl30,rl31,rl32,rl33,rl34,rl35,rl36,rl37,rl38,rl39,rl40,rl41,rl42,rl43,rl44,rl45,rl46,rl47,rl48,rl49,rl50,rl51,rl52,rl53,rl54,rl55,rl56,rl57,rl58,rl59,rl60,rl61,rl62,rl63,rl64,rl65,rl66,rl67,rl68,rl69,rl70,rl71,rl72,rl73,rl74,rl75])
    resulting = ctrl.ControlSystemSimulation(resulting_ctrl)
    
    hasill = []

    df = pd.read_csv('percobaan.csv')
    for index, row in df.iterrows():
        en = row['Energy0']
        ho = row['Homogeneity0']
        ent = row['Entropy0']
        co = row['Contrast0']

        en45 = row['Energy45']
        ho45 = row['Homogeneity45']
        ent45 = row['Entropy45']
        co45 = row['Contrast45']

        en90 = row['Energy90']
        ho90 = row['Homogeneity90']
        ent90 = row['Entropy90']
        co90 = row['Contrast90']

        en135 = row['Energy135']
        ho135 = row['Homogeneity135']
        ent135 = row['Entropy135']
        co135 = row['Contrast135']


        resulting.input['Energy0'] = float(en)
        resulting.input['Homogeneity0'] = float(ho)
        resulting.input['Entropy0'] = float(ent)
        resulting.input['Contrast0'] = float(co)

        # resulting.compute()

        resulting.input['Energy45'] = float(en45)
        resulting.input['Homogeneity45'] = float(ho45)
        resulting.input['Entropy45'] = float(ent45)
        resulting.input['Contrast45'] = float(co45)

        # resulting.compute()

        resulting.input['Energy90'] = float(en90)
        resulting.input['Homogeneity90'] = float(ho90)
        resulting.input['Entropy90'] = float(ent90)
        resulting.input['Contrast90'] = float(co90)

        # resulting.compute()

        resulting.input['Energy135'] = float(en135)
        resulting.input['Homogeneity135'] = float(ho135)
        resulting.input['Entropy135'] = float(ent135)
        resulting.input['Contrast135'] = float(co135)

        resulting.compute()


#================== PRINT RESULT KEMATANGAN ===================================
        #print(resulting.output['result'])
        # result.view(sim=resulting)

        hasill.append(resulting.output['result'])
        prediction = ""
        # kematangan str
        if (resulting.output['result'] > 0.0) and (resulting.output['result'] < 1.00):
            prediction = "Raw Papaya"
            print (resulting.output['result'])
            print('Raw Papaya')
        elif ((resulting.output['result'] >= 1.00) and (resulting.output['result'] < 2.00)):
            prediction = "Medium Papaya"
            print(resulting.output['result'])
            print('Medium Papaya')
        elif (resulting.output['result'] >= 2.00):
            prediction = "Ripe Papaya"
            print(resulting.output['result'])
            print('Ripe Papaya')

        return prediction

