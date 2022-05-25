from .module.model import TransE
import os

wn18rr = TransE(
        ent_tot = 40943,
        rel_tot = 11,
        dim = 1024, 
        p_norm = 1,
        norm_flag = False,
        margin = 6.0)
wn18rr.load_checkpoint(os.path.dirname(__file__) + '/wn18rr.ckpt')

__all__ = ['wn18rr']