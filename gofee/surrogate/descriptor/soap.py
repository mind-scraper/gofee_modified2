from dscribe.descriptors import SOAP

class soap():
    def __init__(self, template_structure=None):
        species = list(set(template_structure.get_chemical_symbols()))
        periodic = template_structure.get_pbc()
        r_cut = 4.0
        n_max = 3
        l_max = 2
        self.descriptor = SOAP(species=species, periodic=periodic.any(), r_cut=r_cut, n_max=n_max, l_max=l_max)

    def get_feature(self, a):
        feature = self.descriptor.create(a)
        return feature
    
    def get_featureGradient(self, a):
        derivatives, descriptors = self.descriptor.derivatives(a)
        return derivatives
