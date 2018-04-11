Chain IN_FedoraWorkstation_allow (1 references)
target     prot opt source               destination         
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:ssh ctstate NEW
ACCEPT     udp  --  anywhere             anywhere             udp dpt:netbios-ns ctstate NEW
ACCEPT     udp  --  anywhere             anywhere             udp dpt:netbios-dgm ctstate NEW
ACCEPT     udp  --  anywhere             224.0.0.251          udp dpt:mdns ctstate NEW
ACCEPT     udp  --  anywhere             anywhere             udp dpts:blackjack:65535 ctstate NEW
ACCEPT     tcp  --  anywhere             anywhere             tcp dpts:blackjack:65535 ctstate NEW



ACCEPT     tcp  --  anywhere             anywhere             tcp dpts:blackjack:65535 ctstate NEW

tgt: 1
prot: 6,6
opt: INGORE
src: 0,0
dst: 0,0
ctstate: NEW, ESTALBISHED, RELATED, INVALID, UNTRACKED

(6,6) ((0,0), (0,0)) (1,1) -> 1

root@somecomp:$ HBPROJ 	-c somechain.txt
						-r somerule.txt

