%load_ext autoreload
%autoreload 2

from anesthetic.anesthetic import MCMCSamples, NestedSamples

samples = MCMCSamples.read('/data/will/data/COM_CosmoParams_base-plikHM_R3.00/base/plikHM_TT_lowl/base_plikHM_TT_lowl')
fig, axes = samples.plot_2d(['H0','tau','omegabh2'],colorscheme='r')

samples = NestedSamples.read('./chains/example')


samples['C'] = samples.B+samples.A
samples.tex['C'] = '$C$'
samples.limits['A']=(-2,2)
samples.limits['B']=(-2,2)

samples.plot_2d(['A','B'])

numpy.repeat([1,2,3],[1,0.5,3])

p = samples.weights
p /= p.sum()
sum(-numpy.log(p)*p)
import matplotlib.pyplot as plt
plt.hist(samples.weights,bins=28)


samples.plot_2d(['A','B'],axes=axes,prior=False,color='b')
samples.plot_2d(['A','B'],color='b')

samples = load_nested_samples('/data/will/data/pablo/runs/chains/planck')
samples.paramnames
h = samples['H0']/100
samples['omegab'] = samples['omegabh2']/h**2
samples.tex['omegab'] = '\Omega_b'
samples['omegac'] = samples['omegach2']/h**2
samples.tex['omegac'] = '\Omega_c'

samples.plot_1d('omegab')

samples.plot_1d(['omegam', 'sigma8', 'theta', 'tau'])
samples.plot_2d( ['omegam', 'omegab', 'omegac'], 'H0')
samples.plot_2d( ['omegam', 'omegab', 'omegac'])



samples_2 = load_nested_samples('/data/will/data/pablo/runs/chains/DES')
samples_3 = load_nested_samples('/data/will/data/pablo/runs/chains/DES_planck')

paramnames = ['omegam', 'sigma8']
fig, axes = samples_2.plot_2d(paramnames, color='b')
samples.plot_2d(paramnames, axes=axes, color='r')
samples_3.plot_2d(paramnames, axes=axes, color='g')

fig, axes = samples_2.plot_2d('omegam', 'sigma8', color='b')
samples.plot_2d('omegam', 'sigma8', axes=axes, color='r')
samples_3.plot_2d('omegam', 'sigma8', axes=axes, color='g')

fig, axes = samples.plot_2d(['omegam', 'omegab', 'omegac'], ['H0','tau'])
for ax in axes.flatten():
    ax.label_outer()

samples.infer()
