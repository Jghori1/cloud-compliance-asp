% ---- Detection rules: what counts as a violation ----

% Rule 1: a public bucket must not hold sensitive data
violation(public_sensitive_bucket(B)) :- bucket(B), public(B), sensitive(B).

% Rule 2: every bucket must be encrypted
violation(unencrypted_bucket(B)) :- bucket(B), not encrypted(B).

% Rule 3: every database must have backups
violation(no_backup(D)) :- database(D), not backup(D).

% Rule 4: every database must be encrypted
violation(unencrypted_db(D)) :- database(D), not encrypted(D).

% Rule 5: a database must not be reachable from the whole internet
% (its security group allows its own port from 0.0.0.0/0)
violation(exposed_db(D)) :-
    database(D), db_port(D,P), db_sg(D,G), ingress(G,P,"0.0.0.0/0").

#show violation/1.