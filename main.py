import sys


# Functie de realizare a inchiderii starilor cu epsilon
def epsilon_closure(state, nfa_trans):
    if (state, "") not in nfa_trans:
        return [state]
    else:
        new_state = nfa_trans[(state, "")]
        for j in new_state:
            if (j, "") in nfa_trans:
                for i_count in range(len(nfa_trans[(j, "")])):
                    if nfa_trans[(j, "")][i_count] not in new_state:
                        new_state.append(nfa_trans[(j, "")][i_count])
        if state not in new_state:
            new_state.append(state)
        return new_state


# extragere alfabet din nfa
def extract_alphabet(nfa_trans):
    alpha = []
    list_keys = list(nfa_transition.keys())

    for k in range(len(nfa_trans)):
        if list_keys[k][1] not in alpha and list_keys[k][1] != "":
            alpha.append(list_keys[k][1])
    return alpha


# Functie de extragere a starilor finale a dfa-ului
def extract_final_state(final_nfa, correspondence):
    final_states_dfa = []
    for m in correspondence:
        for n in final_nfa:
            if int(n) in correspondence[m] and m not in final_states_dfa:
                final_states_dfa.append(m)
    return final_states_dfa


# Functie ce scrie rezultatul in fisier
def write_file(number_state, final_states, dfa_trans):
    f = open(sys.argv[2], "w")
    f.write(str(number_state))
    f.write('\n')
    for counter in range(len(final_states)):
        f.write(str(final_states[counter]))
        if counter < len(final_states) - 1:
            f.write(" ")
    f.write('\n')
    for d in dfa_trans:
        f.write(str(d[0]))
        f.write(" ")
        f.write(str(d[1]))
        f.write(" ")
        f.write(str(dfa_trans[d]))
        f.write('\n')
    f.close()


# Functie ce transforma un NFA in DFA
def transform_in_dfa(final_states_nfa, nfa, alphabet_nfa):
    nr_states = 1  # nr stari dfa
    initial_state = 0  # stare initiala dfa
    dfa = dict()  # salvare tranzitii dfa
    eps_closure = epsilon_closure(initial_state, nfa)  # inchiderea cu eps a starii initiale
    list_states = list()  # lista cu starile din dfa
    list_states.append(initial_state)
    correspondences = dict()  # relatia dintre starile dfa cu cele din nfa:ex {0:[0,1]}
    correspondences[initial_state] = eps_closure

    for j in list_states:
        nfa_state = correspondences[j]
        for c in alphabet_nfa:
            new_states = list()
            for k in nfa_state:
                next_hop = nfa_transition.get((k, c))
                if next_hop is not None:
                    for p in next_hop:
                        if p not in new_states:
                            eps = epsilon_closure(p, nfa_transition)
                            new_states.append(p)
                            for e in eps:
                                if e not in new_states:
                                    new_states.append(e)

            find = 0
            new_states.sort()
            for m in correspondences:
                if correspondences[m] == new_states:
                    dfa[(j, c)] = m
                    find = 1
            if find == 0:
                correspondences[nr_states] = new_states
                dfa[(j, c)] = nr_states
                list_states.append(nr_states)
                nr_states = nr_states + 1

    # extract final state of dfa
    final_states_dfa = extract_final_state(final_states_nfa, correspondences)
    # Scriere in fisier
    write_file(nr_states, final_states_dfa, dfa)


if __name__ == '__main__':

    # citire din fisier
    file = open(sys.argv[1], "r")
    numberOfStates = file.readline()
    finalStates = file.readline().rstrip().split(" ")
    nfa_transition = dict()
    while True:
        transition = file.readline().rstrip().split(" ")
        if transition == ['']:
            break
        if transition[1] == "eps":
            transition[1] = ""

        nfa_transition[(int(transition[0]), transition[1])] = list(map(int, transition[2:]))

    # extragere alfabet
    alphabet = extract_alphabet(nfa_transition)
    # apel functie de transformare
    transform_in_dfa(finalStates, nfa_transition, alphabet)
