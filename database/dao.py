from database.DB_connect import DBConnect

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO

    @staticmethod
    def get_all_hub():
        #restituisce tutti gli hubs
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = '''
            SELECT id, codice, nome, citta, stato, latitudine, longitudine
            FROM hub
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_tratte_connesse():
        #restituisce per ogni coppia di hub: id_hub_1, id_hub_2,
        # somma valore_merce, numero spedizioni
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = '''
                SELECT
                    LEAST(id_hub_origine, id_hub_destinazione) AS hub1,
                    GREATEST(id_hub_origine, id_hub_destinazione) AS hub2,
                    SUM(valore_merce) AS totale_valore,
                    COUNT(*) AS numero_spedizioni
                FROM spedizione
                GROUP BY
                    LEAST(id_hub_origine, id_hub_destinazione),
                    GREATEST(id_hub_origine, id_hub_destinazione);
        ''' # uso GREAT e LEAST per raggruppare correttamente gli hub
            # in modo da avere solo una coppia e non due (siccome a,b è uguale a b,a)

        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result










