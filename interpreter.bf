% settings:
% 0  input
% 1  ptr
% 2  ptr_iterator
% 3  ptr_save
% 4- 15 recursive while
% 16 - inf user data

% change current memory slot is on input
[, % read code
. % print code
---------------------------------------------- % determine .
	% print data in ptr
	[
	> % visit ptr
	[->+>+<<]> % while ptr-- pre_iterator++ and pre_save++
	% now memory slot is on ptr_iterator(2)
	

	-] use - here to end loop
TODO change current momory slot to input
+++++++++++++++++++++++++++++++++++++++++++++++ recover input
]