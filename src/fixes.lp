% ---- Fixes: which fix resolves which violation ----

resolves(make_private(B),   public_sensitive_bucket(B)) :- violation(public_sensitive_bucket(B)).
resolves(move_data(B),      public_sensitive_bucket(B)) :- violation(public_sensitive_bucket(B)).
resolves(encrypt_bucket(B), unencrypted_bucket(B))      :- violation(unencrypted_bucket(B)).
resolves(enable_backup(D),  no_backup(D))               :- violation(no_backup(D)).
resolves(encrypt_db(D),     unencrypted_db(D))          :- violation(unencrypted_db(D)).
resolves(close_port(G,P),   exposed_db(D))              :- violation(exposed_db(D)), db_sg(D,G), db_port(D,P).

% ---- Cost of each fix ----

cost(make_private(B), 3)   :- resolves(make_private(B), _).
cost(move_data(B), 5)      :- resolves(move_data(B), _).
cost(encrypt_bucket(B), 1) :- resolves(encrypt_bucket(B), _).
cost(enable_backup(D), 3)  :- resolves(enable_backup(D), _).
cost(encrypt_db(D), 8)     :- resolves(encrypt_db(D), _).
cost(close_port(G,P), 2)   :- resolves(close_port(G,P), _).

% ---- Choose fixes, then test ----

{ apply(F) : resolves(F, _) }.          % any subset of the possible fixes
fixed(V) :- apply(F), resolves(F, V).   % a violation is fixed if some applied fix resolves it
:- violation(V), not fixed(V).          % every violation must end up fixed

% ---- Optimize: cheapest total ----
#minimize { C,F : apply(F), cost(F, C) }.

#show apply/1.