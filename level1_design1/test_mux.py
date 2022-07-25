# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
A=0
B=1
C=2
D=3

s0 = 1
s1 = 1
s2 = 1
s3 = 1
s4 = 1

#input driving
dut.sel[0].value = s0
dut.sel[1].value = s1
dut.sel[2].value = s2
dut.sel[3].value = s3
dut.sel[4].value = s4

dut.inp0.value = dut.inp4.value = dut.inp8.value = dut.inp12.value = dut.inp16.value = dut.inp20.value = dut.inp24.value = dut.inp28.value = A
dut.inp1.value = dut.inp5.value = dut.inp9.value = dut.inp13.value = dut.inp17.value = dut.inp21.value = dut.inp25.value = dut.inp29.value = B
dut.inp2.value = dut.inp6.value = dut.inp10.value = dut.inp14.value = dut.inp18.value = dut.inp22.value = dut.inp26.value = dut.inp30.value = C
dut.inp3.value = dut.inp7.value = dut.inp11.value = dut.inp15.value = dut.inp19.value = dut.inp23.value = dut.inp27.value = D

await Timer(2, units='ns')

mux_out = sel[4]? (sel[3]? sel[2]? sel[1]? ((sel[0]&inp30) : (sel[0]?inp29:inp28)): sel[1]? ((sel[0]?inp27:inp26) : (sel[0]?inp25:inp24)): (sel[2]? sel[1]? ((sel[0]?inp23:inp22) : (sel[0]?inp21:inp20)): sel[1]? ((sel[0]?inp19:inp18) : (sel[0]?inp17:inp16)))):(sel[3]? sel[2]? sel[1]? ((sel[0]?inp15:inp14) : (sel[0]?inp13:inp12)): sel[1]? ((sel[0]?inp11:inp10) : (sel[0]?inp9:inp8)): (sel[2]? sel[1]? ((sel[0]?inp7:inp6) : (sel[0]?inp5:inp4)): sel[1]? ((sel[0]?inp3:inp2) : (sel[0]?inp1:inp0))))

assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&(~{s1})&(~{s2})&(~{s3})&(~{s4})&{A} != {OUT}, expected value={EXP}".format( A = int(dut.inp0.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =A )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&(~{s1})&(~{s2})&(~{s3})&(~{s4})&{B} != {OUT}, expected value={EXP}".format( B = int(dut.inp1.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =B )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&({s1})&(~{s2})&(~{s3})&(~{s4})&{C} != {OUT}, expected value={EXP}".format( C = int(dut.inp2.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =C )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&({s1})&(~{s2})&(~{s3})&(~{s4})&{D} != {OUT}, expected value={EXP}".format( D = int(dut.inp3.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =D )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&(~{s1})&({s2})&(~{s3})&(~{s4})&{A} != {OUT}, expected value={EXP}".format( A = int(dut.inp4.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =A )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&(~{s1})&({s2})&(~{s3})&(~{s4})&{B} != {OUT}, expected value={EXP}".format( B = int(dut.inp5.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =B )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&({s1})&({s2})&(~{s3})&(~{s4})&{C} != {OUT}, expected value={EXP}".format( C = int(dut.inp6.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =C )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&({s1})&({s2})&(~{s3})&(~{s4})&{D} != {OUT}, expected value={EXP}".format( D = int(dut.inp7.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =D )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&(~{s1})&(~{s2})&({s3})&(~{s4})&{A} != {OUT}, expected value={EXP}".format( A = int(dut.inp8.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =A )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&(~{s1})&(~{s2})&({s3})&(~{s4})&{B} != {OUT}, expected value={EXP}".format( B = int(dut.inp9.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =B )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&({s1})&(~{s2})&({s3})&(~{s4})&{C} != {OUT}, expected value={EXP}".format( C = int(dut.inp10.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =C )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&({s1})&(~{s2})&({s3})&(~{s4})&{D} != {OUT}, expected value={EXP}".format( D = int(dut.inp11.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =D )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&(~{s1})&({s2})&({s3})&(~{s4})&{A} != {OUT}, expected value={EXP}".format( A = int(dut.inp12.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =A )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&(~{s1})&({s2})&({s3})&(~{s4})&{B} != {OUT}, expected value={EXP}".format( B = int(dut.inp13.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =B )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&({s1})&({s2})&({s3})&(~{s4})&{C} != {OUT}, expected value={EXP}".format( C = int(dut.inp14.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =C )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&({s1})&({s2})&({s3})&(~{s4})&{D} != {OUT}, expected value={EXP}".format( D = int(dut.inp15.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =D )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&(~{s1})&(~{s2})&(~{s3})&({s4})&{A} != {OUT}, expected value={EXP}".format( A = int(dut.inp16.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =A )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&(~{s1})&(~{s2})&(~{s3})&({s4})&{B} != {OUT}, expected value={EXP}".format( B = int(dut.inp17.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =B )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&({s1})&(~{s2})&(~{s3})&({s4})&{C} != {OUT}, expected value={EXP}".format( C = int(dut.inp18.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =C )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&({s1})&(~{s2})&(~{s3})&({s4})&{D} != {OUT}, expected value={EXP}".format( D = int(dut.inp19.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =D )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&(~{s1})&({s2})&(~{s3})&({s4})&{A} != {OUT}, expected value={EXP}".format( A = int(dut.inp20.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =A )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&(~{s1})&({s2})&(~{s3})&({s4})&{B} != {OUT}, expected value={EXP}".format( B = int(dut.inp21.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =B )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&({s1})&({s2})&(~{s3})&({s4})&{C} != {OUT}, expected value={EXP}".format( C = int(dut.inp22.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =C )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&(~{s1})&(~{s2})&(~{s3})&({s4})&{D} != {OUT}, expected value={EXP}".format( D = int(dut.inp23.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =D )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&(~{s1})&(~{s2})&({s3})&({s4})&{A} != {OUT}, expected value={EXP}".format( A = int(dut.inp24.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =A )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&(~{s1})&(~{s2})&({s3})&({s4})&{B} != {OUT}, expected value={EXP}".format( B = int(dut.inp25.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =B )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&({s1})&(~{s2})&({s3})&({s4})&{C} != {OUT}, expected value={EXP}".format( C = int(dut.inp26.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =C )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&({s1})&(~{s2})&({s3})&({s4})&{D} != {OUT}, expected value={EXP}".format( D = int(dut.inp27.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =D )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&(~{s1})&({s2})&({s3})&({s4})&{A} != {OUT}, expected value={EXP}".format( A = int(dut.inp28.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =A )
assert dut.out.value == mux_out,"Mux result is incorrect: {s0}&(~{s1})&({s2})&({s3})&({s4})&{B} != {OUT}, expected value={EXP}".format( B = int(dut.inp29.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =B )
assert dut.out.value == mux_out,"Mux result is incorrect: (~{s0})&({s1})&({s2})&({s3})&({s4})&{C} != {OUT}, expected value={EXP}".format( C = int(dut.inp30.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value), EXP =C )


    cocotb.log.info('##### CTB: Develop your test here ########')

@cocotb.test()
async def mux_randomised_test(dut):
    """ Testing the Mux """

   
for i in range(31):
         
dut.sel[0].value = random.randint(0, 1)
dut.sel[1].value = random.randint(0, 1)
dut.sel[2].value = random.randint(0, 1)
dut.sel[3].value = random.randint(0, 1)
dut.sel[4].value = random.randint(0, 1)

dut.sel[0].value = s0
dut.sel[1].value = s1
dut.sel[2].value = s2
dut.sel[3].value = s3
dut.sel[4].value = s4

await Timer(2, units='ns')

dut._log.info(f's0={s0:31} s1= {s1:31} s2={s2:31} s3={s3:31} s4={s4:31} model={mux_out:31} DUT={int(dut.out.value):31}')

assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&(~{s1})&(~{s2})&(~{s3})&(~{s4})&{A} = {OUT}".format( A = int(dut.inp0.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&(~{s1})&(~{s2})&(~{s3})&(~{s4})&{B} != {OUT}".format( B = int(dut.inp1.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&({s1})&(~{s2})&(~{s3})&(~{s4})&{C} != {OUT}".format( C = int(dut.inp2.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&({s1})&(~{s2})&(~{s3})&(~{s4})&{D} != {OUT}".format( D = int(dut.inp3.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&(~{s1})&({s2})&(~{s3})&(~{s4})&{A} != {OUT}".format( A = int(dut.inp4.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value)
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&(~{s1})&({s2})&(~{s3})&(~{s4})&{B} != {OUT}".format( B = int(dut.inp5.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value) )
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&({s1})&({s2})&(~{s3})&(~{s4})&{C} != {OUT}".format( C = int(dut.inp6.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value) )
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&({s1})&({s2})&(~{s3})&(~{s4})&{D} != {OUT}".format( D = int(dut.inp7.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&(~{s1})&(~{s2})&({s3})&(~{s4})&{A} != {OUT}".format( A = int(dut.inp8.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value) )
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&(~{s1})&(~{s2})&({s3})&(~{s4})&{B} != {OUT}".format( B = int(dut.inp9.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&({s1})&(~{s2})&({s3})&(~{s4})&{C} != {OUT}".format( C = int(dut.inp10.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&({s1})&(~{s2})&({s3})&(~{s4})&{D} != {OUT}".format( D = int(dut.inp11.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&(~{s1})&({s2})&({s3})&(~{s4})&{A} != {OUT}".format( A = int(dut.inp12.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&(~{s1})&({s2})&({s3})&(~{s4})&{B} != {OUT}".format( B = int(dut.inp13.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&({s1})&({s2})&({s3})&(~{s4})&{C} != {OUT}".format( C = int(dut.inp14.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&({s1})&({s2})&({s3})&(~{s4})&{D} != {OUT}".format( D = int(dut.inp15.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&(~{s1})&(~{s2})&(~{s3})&({s4})&{A} != {OUT}".format( A = int(dut.inp16.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&(~{s1})&(~{s2})&(~{s3})&({s4})&{B} != {OUT}".format( B = int(dut.inp17.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&({s1})&(~{s2})&(~{s3})&({s4})&{C} != {OUT}".format( C = int(dut.inp18.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&({s1})&(~{s2})&(~{s3})&({s4})&{D} != {OUT}".format( D = int(dut.inp19.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&(~{s1})&({s2})&(~{s3})&({s4})&{A} != {OUT}".format( A = int(dut.inp20.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&(~{s1})&({s2})&(~{s3})&({s4})&{B} != {OUT}".format( B = int(dut.inp21.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&({s1})&({s2})&(~{s3})&({s4})&{C} != {OUT}".format( C = int(dut.inp22.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&(~{s1})&(~{s2})&(~{s3})&({s4})&{D} != {OUT}".format( D = int(dut.inp23.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&(~{s1})&(~{s2})&({s3})&({s4})&{A} != {OUT}".format( A = int(dut.inp24.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&(~{s1})&(~{s2})&({s3})&({s4})&{B} != {OUT}".format( B = int(dut.inp25.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&({s1})&(~{s2})&({s3})&({s4})&{C} != {OUT}".format( C = int(dut.inp26.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&({s1})&(~{s2})&({s3})&({s4})&{D} != {OUT}".format( D = int(dut.inp27.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&(~{s1})&({s2})&({s3})&({s4})&{A} != {OUT}".format( A = int(dut.inp28.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: {s0}&(~{s1})&({s2})&({s3})&({s4})&{B} != {OUT}".format( B = int(dut.inp29.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
assert dut.out.value == mux_out,"Randomised test failed with: (~{s0})&({s1})&({s2})&({s3})&({s4})&{C} != {OUT}".format( C = int(dut.inp30.value), s0 = (dut.sel[0].value), s1 = (dut.sel[1].value),s2 = (dut.sel[2].value),s3 = (dut.sel[3].value),s4 = (dut.sel[4].value),  OUT=int(dut.out.value))
