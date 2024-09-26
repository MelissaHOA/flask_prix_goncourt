from dao.livres_dao import LivresDAO
from services.selection_service import SelectionService
from app.application_console import ApplicationConsole

if __name__ == "__main__":
    livres_dao = LivresDAO(db_path="db/prix_goncourt.db")
    selection_service = SelectionService(livres_dao)

    app = ApplicationConsole(selection_service)
    app.menu()
