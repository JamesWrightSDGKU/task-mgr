from app.database import get_db


def output_formatter(results):
    out = []
    for task in results:
        r_dict = {
            "id": task[0],
            "name": task[1],
            "summary": task[2],
            "description": task[3],
            "is_done": task[4]
        }
        out.append(r_dict)
    return out

def scan():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task", ())
    results = cursor.fetchall()
    return output_formatter(results)

def select_by_id(task_id):
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE id=?", (task_id, )) # comma !
    results = cursor.fetchall()
    if results:
        return output_formatter(results)[0]
    return{}

def create_task(task_data):
    task_tuple = (
        task_data.get("name"),
        task_data.get("summary"),
        task_data.get("description"),
        task_data.get("is_done")
    )
    statement = """
        INSERT INTO task (
            name,
            summary,
            description,
            is_done
        ) VALUES (?, ?, ?, ?)
    """
    conn = get_db()
    conn.execute(statement, task_tuple)
    conn.commit()

def update_by_id(task_data, task_id):
    task_tuple = (
        task_data.get("name"),
        task_data.get("summary"),
        task_data.get("description"),
        task_data.get("is_done"),
        task_id
    )
    statement = """
        UPDATE task
            SET
                name = ?,
                summary = ?,
                description = ?,
                is_done = ?
        WHERE = ?
    """
    conn = get_db()
    conn.execute(statement, task_tuple)
    conn.commit()

def delete_by_id(task_id):
    conn = get_db()
    conn.execute("DELETE FROM task WHERE id=?", (task_id, ))    # comma!
    conn.commit()

def deactivate_task(task_id):
    conn = get_db()
    conn.execute()