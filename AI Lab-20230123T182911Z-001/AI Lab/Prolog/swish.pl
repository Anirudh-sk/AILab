studies(anirudh,cse).
studies(preethivee,cse).
studies(jivitesh,mechanical).
studies(rahuman,mechanical).
studies(srijith,mechanical).
studies(srijith,eee).
teaches(abdul,cse).
teaches(naufel,mechanical).
teaches(naufel,civil).
teaches(murali,eee).


professor(X,Y):-
    teaches(X,C), studies(Y,C).

%teaches(naufel,c), studies(y,c)
%teaches(naufel,mechanical), studies(y,mechanical)
%teaches(naufel,mechanical), studies(jivitesh,mechanical)
%teaches(naufel,mechanical), studies(rahuman,mechanical)
%teaches(naufel,mechanical), studies(srijith,mechanical)
%teaches(naufel,mechanical), studies(y,civil)
%here in the last case the y is falsae cuz no one studies civil