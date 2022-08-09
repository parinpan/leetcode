def wildcard_matching(s, p):
	s_i, p_i = 0, 0
	last_s_i, last_p_i = -1, -1

	while s_i < len(s):
		if p_i < len(p) and (p[p_i] == '?' or s[s_i] == p[p_i]):
			s_i += 1
			p_i += 1

		elif p_i < len(p) and p[p_i] == '*':
			p_i += 1
			last_s_i = s_i
			last_p_i = p_i

		elif last_p_i == -1:
			return False

		else:
			last_s_i += 1
			s_i = last_s_i
			p_i = last_p_i

	while p_i < len(p) and p[p_i] == '*':
		p_i += 1

	return s_i == len(s) and p_i == len(p)

