from django.shortcuts import render
from .forms import *
import random
from array import *

class Mafia():

    def index(request):
        return render(request, 'mafia/index.html')

    def randomizer(request):
        if request.method == 'POST':
            form = PlayersForm(request.POST)
            if form.is_valid():
                players = request.POST.get("players", None)
                room_name = request.POST.get("room_name", None)
                if not room_name:
                    #TO DO: create Model Room(for games history) and insert here Room ID
                    room_name = 'Room #...'
                if players in ["9"]:
                    pl_num = 8;
                    check = False
                if players in ["11"]:
                    pl_num = 10;
                    check = True
                players_list = Mafia.setPlayers(pl_num)
                positions = [None] * pl_num
                for n in range(0, pl_num):
                    positions[n] = n + 1
                return render(request, 'mafia/players_sort.html', {'players_list': players_list,'positions': positions, 'room_name': room_name, 'check': check})
        else:
            form = PlayersForm()
        return render(request, 'mafia/randomizer.html', {'form': form})

    def players_sort(players, player_numbers):
        for t in range(0, player_numbers):
            for a in range(1, player_numbers + 1):
                if players[t] == players[player_numbers - a]:
                    if t != player_numbers - a:
                        players[player_numbers - a] = random.randrange(1, player_numbers + 1)
                        Mafia.players_sort(players, player_numbers)
        return players

    def setPlayers(player_numbers):
        players = [None] * player_numbers
        for n in range(0, player_numbers):
            players[n] = random.randrange(1, player_numbers)
        return Mafia.players_sort(players, player_numbers)
