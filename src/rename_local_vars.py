"""
Author: Alexander Hanel
Version: 1.0
Purpose: Renames local variables to something easier to read
Updates:
    * Version 1.0 Release
"""


import ida_kernwin
import ida_idaapi
import idaapi
import idc
import base64

RENAME_ICON = b"iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAMAAADDpiTIAAAC8VBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
              b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
              b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
              b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
              b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
              b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
              b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
              b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
              b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
              b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" \
              b"AAAAAAAAAAAAAAAAAAAAAAAAAAAACckYSCAAAA+nRSTlMAoNjAuPnccP78/QMBDQIE+/L69/QrCwwX4RXxUgk94oBvMudIIr/oHc2DE" \
              b"2x7Zkec9iAUJN3W63jZ6pc07hEadQatCO3jdNchUTMjQuDbZA+uXgfzuWnp9cx6Eh/JO3KQLFspGxlG5DbwQA6UKBzF5WejJYyOBVlL" \
              b"3tDLZUTD1S8tamLUsyrRT5OJgauNvrFVPHa87MaWMKlYbRCEijVuvWCPusRQFviG70mbr855VoWonYcKHjm2Jk21VFqCTjEYsIunwd9" \
              b"3u5FBJ9pTqn4/c2HTLsc6PjdciF2SoZ9xV1/mY6I40qaemLSVyM+ZRUOkTMKyyqxrSpp9Yh3iIgAADLhJREFUeF7szDEOwVAAANC/N6" \
              b"1Nmg4N0kN06GapzQHEQNLJSCydxcoonMAZ3MHkAF0kZgdwBxPJewd44e8AAAAAAAAAAAAAAAAAAIzn9+vqMjieuu2+OYyWs6yfhN8Vx" \
              b"Wm9qx7FZNEOy9v69Tznva8zppv3h11764nqCsMA/MWkOLNnxmFkKkxnFJWTDkdDkSAMEkC0gBToiMcCCpYWD4hQFLQRsIRDQCYRLdqE" \
              b"NhgbNeIh2ibYC7jQBFOaNu2F2iaevWjUmKYXTb6rmpAQA7L2XnsWndnJ9/yBvZJv7Xe9yVrzcbrkQ931MX+3mMB/RC91lI31tttxus8" \
              b"yD6tbKal8hkzZQ0WfL+loNoHvJA54Mnb/9aUbmZ7vAn6kwoaKSE2pxXU+SPuR1v0BqMwJ/gwgpS7k0NcWmx8M/5f3hs9FWpFDDffaSB" \
              b"Ly0jelPpz1KJj3VcmTAuR2A/iQXFSnsSsXZo35k4Q+VEXaClxIF6qWdG0EZoHh1ctkVO0ycCGN6I2CK82Ck7/65Eb0RgLwIGnorRTnu" \
              b"yCIcVFnGHrJBjxIKQrw7RcggLn4CAoQAhxIsA5FODQ+D7yzMGY9ihAFXMhPKMacow2gXuGWVShGP3AhP6Moa+4vAHVC7tlRlFbgQi6h" \
              b"OH2LC4HfttQgFIezkZJRGwpU5QBO5pxNKFCKEfiQFguK9M/3wOPTFyhS6DbgRS7oUSRrmQGUMnVKKFJYHfAjMSjW0AAo46hCoZLVFQD" \
              b"S3BOFIkl/mkDesl4UKmlwD6hEzAf719qSrRIKEpoGcjxWFERv2XirZst28B7JSq98//c7t//9sbg2o7PtNzeqFXQXmIxOHaqVvTyzZ+" \
              b"7hHY7wXwa2R+wsbIBZQ6Jzx399vREsyK+e1QVNvSoHf3rYF49USXR+7A0X8tmQDjOpW4l8qrrLftgFPkWMFUcTVvIEd8BMpTz+PCo3/" \
              b"+Pyy8vAT5D0C85jgaiQ5Sy8TYaEClmKckqzwM+QrR+eUbgHdI9hujFUxnr1A38dPkmMO65HBaQDMNU5VGJFt+c6+DPyXUmkhLICp54C" \
              b"sSgv6OKpBeD/SISCi9x34uFN91GWy5kIGkFGu+yyYV4Nk6AW5TzKMYGGkK9lH3O5n05+4A8dshXEfQQaQxbG7EMmVx5MCNcjU/sDA2g" \
              b"QMZWzJ7t84rdezc4K9xLNjp/kbkaW3fCa4SayXNwL2kUM31iQwQMAV5AhtAO0jVQW4czseRDPKIC6wWDQPFLGaAJD6xgFwD78Hzt3rw" \
              b"tdGIZhlHwhfsbMl0nIFBITIqIgGhIJkiEqOolWoRDEWWg5AYWg0YlKolNItKJSKBUaUYpKL3v27N0+75p1BneuYhfvPMYL4TPn2EjO8" \
              b"79FT7mi2Dj+Kf+7OzNcGEMPpQN4rZotkMp3yQBmbRZL9atUADsWi2ZwtUQATXvF07ovHMCltSJa+1cwgLeKsUJqFDv1NL1lqqA2i7z7" \
              b"3Z80VFjNAgGMmimuaufPgCcrRXZU73RSyrvf2E7c9E3bYf7NiVMLRfecF8B/x1zCq7y76Z22i5wnYLvmia/V/vT7R/QByP8f6IFxUtB" \
              b"o90h03jZpuGoTwHXas/gMfDFNGlayT0qNWSYV2dfgbg2Tiu7MAM4Nk4rtzACWDJOK8awA6jXDpKKW9RU4YZd0ZD0LeTRLOnqyTgj/HQ" \
              b"ABIAAEgAAQAAJAAAgAASAABIAAEAACQAAIAAEgAASAABAAAkAACAABIAAEgAAQAAJAAAgAASAABIAAEAACQAAIAAEgAASAABAAAvhll" \
              b"w4JAABAGIBxQQDaPBH99RUFMHcIlmGE6bUfoHAAYzPs18EJgDAURMHAR6KeJEXYf3052YCg4iXkz6thDrvRP6b6BGDQAoC7ABAAAkAA" \
              b"CAAB8DMAjtwAANhzAwBgzQ0AgC0xAABsAADaBADkBgoAASAABMAUAXC+BnCxS8ckAAAgFETlwAY/mf2TOFlABBcnX4IbTgxe7Adwjqm" \
              b"JKHbt4AQAEIiBoOBp//X6sgXBV46ZGpa88r4ANcJ5BZcAvggAASAABIAAEAACQAAIAAEgAASAABAAAkAACAABIAAEgADyCQABIAAEgA" \
              b"AQAAJAAAgAASAABIAAEAACQAAIAAEgAASAADoQAAJAAAgAASAABIAAEAACQAAIAAEgAASAABAAAkAACAAB5BMAAkAACAABIAAEgAAQA" \
              b"AJAAAgAASAABIAAEAACQAAIAAF0IAAEgAAQAAJAAAgAASAABIAAEAACQAAIAAEgAASAABAAAsgnAASAABAAAkAACAABIAAEgAAQAAJA" \
              b"AAgAASAABIAAEAAC6EAACAABIAAEgAAQAAJAAAgAASAABIAAEAACQAAIAAEgAASQTwAIAAEgAASAABAAAkAACAABIAAEgAAQAAJAAAg" \
              b"AASAABNCAABAAAkAACAABIAAEgAAQAAJAAAgAAeQTwGWXjmkAAEAYgJERHEwZ/pXswgAh4eGiGtoFIAYv9wECx1js17EJACEURMGDQ0" \
              b"Qj+y/VyA4URBC+w2thgt1dAFqX1wDudwyAABAAAkAACAABMA+A9jYAAOrDAAAAAIASCIBsAHkBAkAACAABIABCBcBgrw4JAABAIIjxg" \
              b"gC0uUT01ygyvEOwEkOm134BpQNY9u6fpcowDuP4BVqcyPwDwYkiD5whBw0RXFrUA5YuDtEQYUoIgU5FW4P0Z2koGgSF3oAOgTSloIuF" \
              b"U9Cma+/jmnoD9/2c54znd38/r+E7XnApIFbBIAAQAAgABAACAAGAAEAAIAAQAAgABAACAAGAAEAAIAAQAAgABAACAAGAAEAAIAAQAAg" \
              b"ABAACAAGAAEAAIAAQAAgABAACAAGAAEAAIAAQAAgABAACAAHkEcC5gkP1ceRrlQKTThhTKbDtlH0VAjtOmVYh8NsphyoEHjjli8qAZS" \
              b"dNDKsIeOS0dRUBu077pRJgtuG01ogKgBfO+ab40LzjnDXFhynnXSg6PHnrvCNFhwVXmVZsuL3lKu+uKzTsudpHRYbxa662OK+4sPrQ3" \
              b"XwdVlg4c3f3FRWmXMPoT8WEzQPXsbKviPBh0fV8mlM8OJ5wXWs3FA2et1zfwF3FgpdX3YujjiLB+xX35tUtxYGTm+5Vq60gMPS54d7N" \
              b"/FMIaD523qDzfgyp/2F8yXlvOs+cd+9YfQ5z3xvO+9PU7JjzDv521M9w+tQVrrQlbbjK0qX6Fv6zV68tUbVRHIcXgrG3TmPNNJMzNub" \
              b"ojI2apqNZaqFYnsoDD2WeErRzRqaBhyxHSLNIKMzCSuMpMkLqTR4iqKznMZSMgqAIyqAorNdBQetVYBCGsmfuvW91Btb1BX5v/uu+rf" \
              b"koyTwZeI9ShOgS8EjEvz8GJZ2FSfp4lJSYvhA8DtmcpEVpjgH4zZaD0taHG8GjkOCLIjpRdOBPIC4EnSh8Nwgeg2RfR6daIqYEdOfRm" \
              b"UXjreAJSPnDDHRuwW6Yal0AOiUcMu8C90Z0bRnoijQ7/C0wBl0g9PybDO6K6ILi0TUFY9MCFm90ieC47IYbIPZLZU3oqpN2mO7uCnSR" \
              b"4OiujwV3QfQVa/9bgQxS9TCTyjBkkPvpeLAfzC+ypfXa1wYRmQhtKpiZaRjZFD45nWVTw5wjpoOrqvsnLlQJyKzwvkSgWEBmmtVXv7z" \
              b"4UGH3g1lD1Hrj9p2b2vfceJBnvvK8tABlM3SClKHFKJdo+HY4fGXzpaHG151jtgiTChQjqn3hrxLSNmqRl1AjSNM9Q06EwjUGr6KyYJ" \
              b"CLBEaHIFe9Uc7PckO3BrlqGqkEOUi9Bvm6+BhcUX4B+brZDuzIUy1yZagHF6m2BSBXa6zAinzeijyJNXqGePJ35CqjC9gQ/17kKWwTs" \
              b"Blajjx1+AETsgM58nrpC6z0kYnIUTYwIdHITWmWGuQw/TiC3KQDE7IaOcl/CrL51jUgJxPAggwiF+KdR6CMJRS58AIW5BRyoE3aDMq9" \
              b"+UdA5XyWAgOSjEotGj0WAXzYU44qHyPbAEgLKiGORsUCT5nnFG7gNjAhNSib2BFlBP4yzxWhfHXAhFhQHp+r1UaYLdaRMJQnhvEHIKa" \
              b"9yGx/fpClBGbXrmX/92iRWSowInFVyECI78vTqWFu1O4zD+cgiwQ7sCL3PjIcfhfMtd0MT8GrWGBHxkJQkmZBR9/Pt4E2FcwXv7jGvO" \
              b"7DjjQflHRiAOQgtpQzGpzOO3f0VuSO9ko1uItaa3Zz2/gTg4jTLQkt/tWeHeIgCAYAGKU7RjU4BxfAC1BsMoMmOsHNDaJn8Ag/G5sXI" \
              b"BDIWq1WjuAxvIPJzfeu8MVvEX2LuAxTe0uf/eFebtbFdbdsfnmsbo+nfX1+Das5z8bHJbyr7k/qAwAAAAAAAAAAAAAAAAAfO8Ta8Itx" \
              b"h4YAAAAASUVORK5CYII="

RENAME_ICON_32 = ida_kernwin.load_custom_icon(data=base64.b64decode(RENAME_ICON), format="png")


class RENAMER(ida_kernwin.action_handler_t):
    def __init__(self):
        ida_kernwin.action_handler_t.__init__(self)
        return

    def update(self, ctx):
        return ida_kernwin.AST_ENABLE_ALWAYS

    def activate(self, ctx):
        word_list = ['abacus', 'aeon', 'alpha', 'arc', 'atlas', 'baryon', 'beta', 'carat', 'ceres', 'chaos', 'chi',
                     'dean', 'delta', 'epsilon', 'eta', 'fermat', 'gamma', 'gaudi', 'gnomen', 'ides', 'iota', 'iris',
                     'julia', 'kappa', 'kite', 'lambda', 'lemma', 'locus', 'lune', 'mars', 'mu', 'nocebo', 'nu',
                     'occam', 'ogive', 'omega', 'omicron', 'pareto', 'pascal', 'phi', 'pi', 'psi', 'rho', 'sabot',
                     'secant', 'sigma', 'simson', 'surd', 'tare', 'tau', 'theta', 'umbra', 'upsilon', 'venus', 'xenon',
                     'xi', 'zeta', 'zipf']

        func = idaapi.get_func(idc.here())
        frame = idaapi.get_frame(func)

        for mid in range(frame.memqty):
            var_name = idc.get_member_name(frame.id, frame.get_member(mid).soff)
            if not var_name.startswith("var_"):
                continue
            if len(word_list) < mid:
                print("exceeded variable names.. exiting ")
                break
            idc.set_member_name(frame.id, frame.get_member(mid).soff, "_" + word_list[mid])
        idaapi.request_refresh(0xFFFFFFFF)
        return

    def term(self):
        pass


class RenameLocalVarsPlugin(ida_idaapi.plugin_t):
    flags = ida_idaapi.PLUGIN_KEEP
    comment = "Rename local variables"
    help = "Renames local variables to something more friendly"
    wanted_name = "Rename Local Variables"
    wanted_hotkey = ""

    def init(self):
        self.actions = [
            ida_kernwin.action_desc_t(
                "rename_vars",
                "Rename Local Variables",
                RENAMER(),
                "Shift-Alt-r",
                "Rename local variables",
                RENAME_ICON_32
            )
        ]
        for action_desc in self.actions:
            ida_kernwin.register_action(action_desc)

        self.menus = Menus()
        self.menus.hook()

        return ida_idaapi.PLUGIN_KEEP

    def run(self, arg):
        return

    def term(self):
        if self.actions:
            for action_desc in self.actions:
                ida_kernwin.unregister_action(action_desc.name)


class Menus(ida_kernwin.UI_Hooks):
    def finish_populating_widget_popup(self, form, popup):
        if ida_kernwin.get_widget_type(form) == ida_kernwin.BWN_DISASM:
            ida_kernwin.attach_action_to_popup(form, popup, "rename_vars", "Rename Local Variables")


def PLUGIN_ENTRY():
    return RenameLocalVarsPlugin()
