# Import von Kennwort.py

import Kennwort

# Wichtig: Der Modulname muss vorangestellt werden
print(Kennwort.Kennwort(24))

from Kennwort import Kennwort
# Jetzt muss der Modulname nicht mehr vorangestellt werden
print(Kennwort(4))
