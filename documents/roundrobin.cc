#include <iostream>
#include <vector>
#include <array>
#include <string>

using namespace std;

vector<char> teams;
void getteams()
{
	int flag=0;
	char check='A';
	cout<<"How many teams would you like to enter? ";
	cin>>flag;
	for(int i=0;i<flag;i++)
	{
		teams.push_back(check);
		check++;
	}
}
//this is the actual meat of the code
void creategames()
{
	//initialize vairables
	int flag=0,stuff;
	//figure out the necessary size of the team array
	if(teams.size()%2==0){stuff=teams.size();}
	else{stuff=teams.size()+1;}
	string team[stuff];
	string temp[stuff];
	//copy the elements into the team array
	for(int a=0;a<teams.size();a++)
	{
		team[a]=teams[a];
	}
	//if there's an odd number of teams add a bye team
	if(teams.size()%2==1)
	{
		team[team.size()-1]="Bye";
	}
	//copy a static player one
	temp[0]=team[0];
	while(flag<team.size()-1)
	{
		//begin major logic for building the days
		cout<<"Day "<<flag+1<<endl;
		for(int i=0,j=team.size()-1;i<teams.size()/2;i++,j--)
		{
			//print out a game
			cout<<team[i]<<" Plays "<<team[j]<<endl;
		}
		//shuffle the teams in the array to do the thing again without repeating games
		for(int z=1;z<team.size();z++)
		{
			if(z=team.size()-1)
			{
				temp[1]=team[z];
			}
			else
			{
				temp[z+1]=team[z];
			}
		}
		team=temp;
	}
}



int main()
{
	getteams();
	creategames();
	return 0;
}