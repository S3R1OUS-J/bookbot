def num_of_words(text):
    words = text.split()
    num_words = len(words)
    return(num_words)

def sort_on(items):
    return items["num"]

def chr_count(text):
    lower_case_text = text.lower()
    a_count = lower_case_text.count('a')
    b_count = lower_case_text.count('b')
    c_count = lower_case_text.count('c')
    d_count = lower_case_text.count('d')
    e_count = lower_case_text.count('e')
    f_count = lower_case_text.count('f')
    g_count = lower_case_text.count('g')
    h_count = lower_case_text.count('h')
    i_count = lower_case_text.count('i')
    j_count = lower_case_text.count('j')
    k_count = lower_case_text.count('k')
    l_count = lower_case_text.count('l')
    m_count = lower_case_text.count('m')
    n_count = lower_case_text.count('n')
    o_count = lower_case_text.count('o')
    p_count = lower_case_text.count('p')
    q_count = lower_case_text.count('q')
    r_count = lower_case_text.count('r')
    s_count = lower_case_text.count('s')
    t_count = lower_case_text.count('t')
    u_count = lower_case_text.count('u')
    v_count = lower_case_text.count('v')
    w_count = lower_case_text.count('w')
    x_count = lower_case_text.count('x')
    y_count = lower_case_text.count('y')
    z_count = lower_case_text.count('z')
    space_count = lower_case_text.count(' ')
    period_count = lower_case_text.count('.')
    question_count = lower_case_text.count('?')
    point_count = lower_case_text.count('!')
    colon_count = lower_case_text.count(':')
    semi_colon_count = lower_case_text.count(';')
    æ_count = lower_case_text.count('æ')
    â_count = lower_case_text.count('â')
    ê_count = lower_case_text.count('ê')
    ë_count = lower_case_text.count('ë')
    ô_count = lower_case_text.count('ô')

    num_chr = {
            "a": a_count,
            "b": b_count,
            "c": c_count,
            "d": d_count,
            "e": e_count,
            "f": f_count,
            "g": g_count,
            "h": h_count,
            "i": i_count,
            "j": j_count,
            "k": k_count,
            "l": l_count,
            "m": m_count,
            "n": n_count,
            "o": o_count,
            "p": p_count,
            "q": q_count,
            "r": r_count,
            "s": s_count,
            "t": t_count,
            "u": u_count,
            "v": v_count,
            "w": w_count,
            "x": x_count,
            "y": y_count,
            "z": z_count,
            " ": space_count,
            ".": period_count,
            "?": question_count,
            "!": point_count,
            ":": colon_count,
            ";": semi_colon_count,
            "æ": æ_count,
            "â": â_count,
            "ê": ê_count,
            "ë": ë_count,
            "ô": ô_count,
    }
    return num_chr

def sorted_list(num_chr):
    chr_list = [
        {"char": "a", "num": num_chr["a"]},
        {"char": "b", "num": num_chr["b"]},
        {"char": "c", "num": num_chr["c"]},
        {"char": "d", "num": num_chr["d"]},
        {"char": "e", "num": num_chr["e"]},
        {"char": "f", "num": num_chr["f"]},
        {"char": "g", "num": num_chr["g"]},
        {"char": "h", "num": num_chr["h"]},
        {"char": "i", "num": num_chr["i"]},
        {"char": "j", "num": num_chr["j"]},
        {"char": "k", "num": num_chr["k"]},
        {"char": "l", "num": num_chr["l"]},
        {"char": "m", "num": num_chr["m"]},
        {"char": "n", "num": num_chr["n"]},
        {"char": "o", "num": num_chr["o"]},
        {"char": "p", "num": num_chr["p"]},
        {"char": "q", "num": num_chr["q"]},
        {"char": "s", "num": num_chr["s"]},
        {"char": "t", "num": num_chr["t"]},
        {"char": "u", "num": num_chr["u"]},
        {"char": "v", "num": num_chr["v"]},
        {"char": "w", "num": num_chr["w"]},
        {"char": "x", "num": num_chr["x"]},
        {"char": "y", "num": num_chr["y"]},
        {"char": "z", "num": num_chr["z"]},
        {"char": "æ", "num": num_chr["æ"]},
        {"char": "â", "num": num_chr["â"]},
        {"char": "ê", "num": num_chr["ê"]},
        {"char": "ë", "num": num_chr["ë"]},
        {"char": "ô", "num": num_chr["ô"]}
    ]
    chr_list.sort(reverse=True, key=sort_on)
    return chr_list
        
