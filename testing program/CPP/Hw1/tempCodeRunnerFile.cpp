  for (unsigned int count = 0; count < Nodes; count++){
        cout << count << endl;
        for (unsigned int count2 = 0; count2<Destinations; count2++){
            ID = DES[count2]; // Destination's ID
            cout << ID << " ";
            if(!node[count].isSDN) // if the node is not SDN
                cout << node[count].table[ID][0].first; //next point
            else{ // index = ID, (next point+balance)
                for(auto const& p: node[count].table[ID]){// 下一個點&權重
                    cout << p.first << " " << p.second * 100 << "% ";
                }
            }
            cout<<endl;   
        }
    }