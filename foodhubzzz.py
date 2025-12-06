from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from typing import Optional, Dict
from datetime import datetime
import os
import hashlib

from algoz import Shop
from tempz import get_base_html, PRIMARY_RED, ACCENT_ORANGE

app = FastAPI()

static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

sessions_db: Dict[str, dict] = {}

shops = {}

s1 = Shop('s1', "Baby's Eatery", 'hesoyam')
s1.status = 'Open'
s1.add_category('Ulam')
s1.add_item('Ulam', 'u1', 'Lechon Kawali', 50.0)
s1.add_item('Ulam', 'u2', 'Pork Sisig', 50.0)
s1.add_category('Softdrinks')
s1.add_item('Softdrinks', 's1', 'Mt. Dew', 25.0)
s1.add_item('Softdrinks', 's2', 'Pepsi', 25.0)
s1.add_item('Softdrinks', 's3', 'Cobra', 25.0)


s2 = Shop('s2', 'Juice Bar', 'stinglikeabee')
s2.add_category('Drinks')
s2.add_item('Drinks', 'd1', 'Iced Tea', 60.0)
s2.add_item('Drinks', 'd2', 'Unsweetened Iced Tea', 60.0)


s3 = Shop('s3', 'Dunk-it Donuts', 'baguvix')
s3.status = 'Open'
s3.add_category('Donuts')
s3.add_item('Donuts', 'd1', 'Choco BTN', 35.0)
s3.add_item('Donuts', 'd2', 'Bavarian', 35.0)
s3.add_category('Beverages')
s3.add_item('Beverages', 'b1', 'Coffee', 39.0)
s3.add_category('Combo')
s3.add_item('Combo', 'c1', 'Any Donut + Coffee', 70.0)

s4 = Shop('s4', 'Alec Kalbonara', '1234')
s4.add_category('Meals')
s4.add_item('Meals', 'mm1', 'Kalbonara', 60.0)
s4.add_item('Meals', 'mm2', 'Kalbonara Pro', 80.0)
s4.add_item('Meals', 'mm3', 'Kalbonara Pro Max', 100.0)

shops[s1.shop_id] = s1
shops[s2.shop_id] = s2
shops[s3.shop_id] = s3
shops[s4.shop_id] = s4


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    session_id = request.cookies.get("session_id")
    if session_id and session_id in sessions_db:
        return RedirectResponse(url="/shops", status_code=302)
    return RedirectResponse(url="/login", status_code=302)


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    shop_options = "".join([f'<option value="{shop.shop_id}">{shop.name}</option>' for shop in shops.values()])

    params = request.query_params
    error_msg = params.get('error', '')
    error_html = f'<div class="error-message">{error_msg}</div>' if error_msg else ''

    if params.get('v') == '1':
        content = f'''
        <div class="login-container">
            <div class="login-card" style="text-align: center;">
                <h1 class="big-title" style="justify-content: center;"><img src="/static/logo4.png" alt="FoodHub Pro Max" class="logo-image login-logo"></h1>
                <p style="color: #555; margin-bottom: 18px; font-size: 1.05rem;">Vendor sign in</p>
                {error_html}
                <form method="POST" action="/login">
                    <input type="hidden" name="role" value="vendor">
                    <div class="form-group">
                        <select name="shop_id" required>
                            <option value="">Select Shop</option>
                            {shop_options}
                        </select>
                    </div>
                    <div class="form-group">
                        <input type="password" name="password" placeholder="Password" required>
                    </div>
                    <button type="submit" class="btn btn-primary" style="width: 100%;">Login as Vendor</button>
                </form>
                <div style="margin-top:12px; text-align:center;"><a href="/login" class="btn btn-primary" style="text-decoration:none; background-color: {ACCENT_ORANGE};">Back</a></div>
            </div>
        </div>
        '''
        return get_base_html("Vendor Login - FoodHub", content, show_header=False)

    content = f'''
    <div class="login-container">
        <div class="login-card" style="text-align: center;">
            <h1 class="big-title" style="justify-content: center;"><img src="/static/logo4.png" alt="FoodHub Pro Max" class="logo-image login-logo"></h1>
            <p style="color: #555; margin-bottom: 20px; font-size: 1.05rem;">Are you a customer or a shop owner?</p>
            <div class="login-role-buttons">
                <a href="/shops" class="login-role-btn customer">Customer</a>
                <a href="/login?v=1" class="login-role-btn vendor">Vendor / Shop Owner</a>
            </div>
        </div>
    </div>
    '''

    return get_base_html("Login - FoodHub", content, show_header=False)


@app.post("/login", response_class=HTMLResponse)
async def login_submit(request: Request, role: str = Form(...), email: str = Form(None), password: str = Form(...),
                       shop_id: str = Form(None)):
    if role == 'customer':
        return RedirectResponse(url="/shops", status_code=302)

    # vendor login
    shop = shops.get(shop_id)
    if shop and shop.password == password:
        session_id = hashlib.md5(f"{shop_id}{datetime.now()}".encode()).hexdigest()
        sessions_db[session_id] = {"role": "vendor", "current_shop": shop_id}
        response = RedirectResponse(url="/dashboard", status_code=302)
        response.set_cookie("session_id", session_id, max_age=86400)
        return response

    error = "Invalid shop ID or password. Please try again."
    return RedirectResponse(url=f"/login?v=1&error={error}", status_code=302)


@app.get("/shops", response_class=HTMLResponse)
async def shops_list(request: Request):
    session_id = request.cookies.get("session_id")
    session = sessions_db.get(session_id) if session_id else None

    shops_html = "".join([f'''
    <div class="shop-card">
        <div class="shop-info">
            <h3>{shop.name}</h3>
            <p>Status: {shop.status} • ID: {shop.shop_id}</p>
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">
            <span class="status-badge {shop.status.lower()}">{shop.status}</span>
            <a href="/shop/{shop.shop_id}" class="btn btn-primary btn-small">View Menu</a>
        </div>
    </div>
    ''' for shop in shops.values()])

    content = f'<h2 class="section-title">Available Shops</h2><div class="shops-grid">{shops_html}</div>'

    return get_base_html("Shops - FoodHub", content, authenticated=bool(session),
                         role=session.get('role') if session else None)


@app.get("/shop/{shop_id}", response_class=HTMLResponse)
async def shop_detail(request: Request, shop_id: str):
    shop = shops.get(shop_id)
    if not shop:
        return RedirectResponse(url="/shops", status_code=302)

    session_id = request.cookies.get("session_id")
    session = sessions_db.get(session_id) if session_id else None

    categories_html = ""
    shop_is_closed = shop.status.lower() == "closed"
    for node, _ in shop.menu_tree.traverse_preorder():
        items = node.items_list.to_list()
        if items:
            if shop_is_closed:
                items_html = "".join([f"""
                <div class=\"item-card\">\n                    <div class=\"item-info\">\n                        <h4>{item.name}</h4>\n                        <p style=\"font-size: 0.8rem; color: #666;\">Category: {node.name} | ID: {item.item_id}</p>\n                    </div>\n                    <div>\n                        <span style=\"font-weight: 700; color: #888; margin-right: 10px;\">N/A</span>\n                        <span class=\"item-status sold-out\">N/A</span>\n                    </div>\n                </div>\n                """ for item in items])
            else:
                items_html = "".join([f"""
                <div class=\"item-card\">\n                    <div class=\"item-info\">\n                        <h4>{item.name}</h4>\n                        <p style=\"font-size: 0.8rem; color: #666;\">Category: {node.name} | ID: {item.item_id}</p>\n                    </div>\n                    <div>\n                        <span style=\"font-weight: 700; color: {PRIMARY_RED}; margin-right: 10px;\">₱{item.price:.2f}</span>\n                        <span class=\"item-status {'available' if item.available else 'sold-out'}\">{'Available' if item.available else 'Sold Out'}</span>\n                    </div>\n                </div>\n                """ for item in items])
            categories_html += f"<div class=\"category-section\"><div class=\"category-name\">{node.name}</div>{items_html}</div>"
    updates_html = "".join([f'<div class="update-item">{u}</div>' for u in reversed(shop.recent_updates.get())])
    overlay_html = """
    <div class='shop-closed-overlay'>Shop is Closed</div>
    """ if shop_is_closed else ""
    status_class = {
        "open": "open",
        "preparing": "preparing",
        "closed": "closed"
    }.get(shop.status.lower(), "closed")
    content = f'''
    <div style="position: relative;">
        {overlay_html}
        <h1>{shop.name}</h1>
        <p style="color: #666;">Status: <span class="status-badge {status_class}">{shop.status}</span></p>
        <div style="display:flex; gap:20px; align-items:flex-start;">
            <div style="flex:1;">
                {categories_html if categories_html else '<p class="empty-message">No items yet.</p>'}
            </div>
            <aside class="sidebar-updates">
                <div class="sidebar-title">📋 Recent Updates</div>
                <div>{updates_html if updates_html else '<p class="empty-message">No updates</p>'}</div>
            </aside>
        </div>
    </div>
    '''

    extra_head = '<meta http-equiv="refresh" content="5">'
    return get_base_html(f"{shop.name} - Menu", content, authenticated=bool(session),
                         role=session.get('role') if session else None, extra_head=extra_head)


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, query: Optional[str] = None):
    session_id = request.cookies.get("session_id")
    session = sessions_db.get(session_id) if session_id else None

    q = (query or "").strip().lower()
    shop_results_html = ""
    item_results_html = ""

    if q:
        for shop in shops.values():
            if q in shop.name.lower() or q in shop.shop_id.lower():
                shop_results_html += f"""
                <div class=\"shop-card\">
                    <div class=\"shop-info\">
                        <h3>{shop.name}</h3>
                        <p>ID: {shop.shop_id}</p>
                    </div>
                    <div style=\"display: flex; gap: 10px;\">
                        <span class=\"status-badge {shop.status.lower()}\">{shop.status}</span>
                        <a href=\"/shop/{shop.shop_id}\" class=\"btn btn-primary btn-small\">View Menu</a>
                    </div>
                </div>
                """

        for shop in shops.values():
            shop_items = [(node.name, item) for node, _ in shop.menu_tree.traverse_preorder() for item in
                          node.items_list.to_list() if q in item.name.lower() or q in item.item_id.lower()]
            if shop_items:
                items_html = "".join([f"""
                <div class=\"item-card\">
                    <div class=\"item-info\">
                        <h4>{item.name}</h4>
                        <p style=\"font-size: 0.8rem; color: #666;\">Category: {cat_name} | ID: {item.item_id}</p>
                    </div>
                    <div>
                        <span style=\"font-weight: 700; color: {PRIMARY_RED}; margin-right: 10px;\">₱{item.price:.2f}</span>
                        <span class=\"item-status {'available' if item.available else 'sold-out'}\">{'Available' if item.available else 'Sold Out'}</span>
                    </div>
                </div>
                """ for cat_name, item in shop_items])
                item_results_html += f'<div style="margin-bottom: 20px;"><h4 style="color: {PRIMARY_RED}; margin-bottom: 10px;">{shop.name} ({len(shop_items)} items)</h4>{items_html}</div>'

    content = f'''
    <h2 class="section-title">Search Shops & Items</h2>

    <div class="search-form">
        <form method="GET" action="/search">
            <input type="text" name="query" placeholder="Search..." value="{query or ''}" required>
            <button type="submit" class="btn btn-primary">Search</button>
        </form>
    </div>

    {shop_results_html if shop_results_html else ''}
    {item_results_html if item_results_html else ''}
    {f'<div class="empty-message">No results for "{query}"</div>' if query and not shop_results_html and not item_results_html else ''}
    {'' if query else '<div class="empty-message">Enter a shop/item</div>'}
    '''

    return get_base_html("Search - FoodHub", content, authenticated=bool(session),
                         role=session.get('role') if session else None)


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    session_id = request.cookies.get("session_id")
    if not session_id or session_id not in sessions_db:
        return RedirectResponse(url="/login", status_code=302)

    session = sessions_db.get(session_id, {})
    if session.get('role') != 'vendor':
        return RedirectResponse(url="/shops", status_code=302)

    shop = shops.get(session.get('current_shop'))
    if not shop:
        return RedirectResponse(url="/shops", status_code=302)

    categories_options = "".join(
        [f'<option value="{cat}">{cat_node.name}</option>' for cat, cat_node in shop.menu_tree.children.items()])

    items_html = ""

    for cat_name, cat_node in shop.menu_tree.children.items():
        items = cat_node.items_list.to_list()
        items_html += f'<h4 style="margin-top: 15px; color: {PRIMARY_RED};">{cat_node.name}</h4>'
        if items:
            for item in items:
                items_html += f'''
                <div class="item-management-row">
                    <div><strong>{item.name}</strong><p style="font-size: 0.8rem; color: #666;">ID: {item.item_id}</p></div>
                    <div>₱{item.price:.2f}</div>
                    <div><span class="item-status {'available' if item.available else 'sold-out'}">{'Available' if item.available else 'Sold Out'}</span></div>
                    <div style="display: flex; gap: 8px;">
                        <form method="POST" action="/toggle-availability" style="display:inline;">
                            <input type="hidden" name="category" value="{cat_name}">
                            <input type="hidden" name="item_id" value="{item.item_id}">
                            <button type="submit" class="btn btn-warning btn-small">Toggle</button>
                        </form>
                        <form method="POST" action="/remove-item" style="display:inline;">
                            <input type="hidden" name="category" value="{cat_name}">
                            <input type="hidden" name="item_id" value="{item.item_id}">
                            <button type="submit" class="btn btn-danger btn-small" onclick="return confirm('Remove?')">Remove</button>
                        </form>
                    </div>
                </div>
                '''
        else:
            items_html += '<p class="empty-message">No items in this category</p>'

    updates_html = "".join(
        [f'<div class="update-item">{update}</div>' for update in reversed(shop.recent_updates.get())])

    error_msg = session.get('error', '')
    error_html = f'<div class="error-message">⚠️ {error_msg}</div>' if error_msg else ''

    content = f'''
    <div class="dashboard-layout">
        <div>
            {error_html}
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px;">
                <div class="dashboard-shop-title">{shop.name}</div>
                <div class="status-selector">
                    <span style="font-weight: 600; color: #666;">Status:</span>
                    <form method="POST" action="/update-status" style="display: flex; gap: 8px;">
                        <button type="submit" name="status" value="Open" class="status-btn open {'active' if shop.status == 'Open' else ''}">Open</button>
                        <button type="submit" name="status" value="Preparing" class="status-btn preparing {'active' if shop.status == 'Preparing' else ''}">Preparing</button>
                        <button type="submit" name="status" value="Closed" class="status-btn closed {'active' if shop.status == 'Closed' else ''}">Closed</button>
                    </form>
                </div>
            </div>

            <h2 class="section-title">Menu Management</h2>

            <div style="display: grid; gap: 15px;">
                <div class="management-card">
                    <h3>Add Category</h3>
                    <form method="POST" action="/add-category">
                        <input type="text" name="category_name" placeholder="Category Name" required>
                        <button type="submit" class="btn btn-primary" style="width: 100%;">Add</button>
                    </form>
                </div>

                <div class="management-card">
                    <h3>Add Item</h3>
                    {f'''<form method="POST" action="/add-item">
                        <select name="category" required>
                            <option value="">Select Category</option>
                            {categories_options}
                        </select>
                        <input type="text" name="item_id" placeholder="Item ID" required>
                        <input type="text" name="item_name" placeholder="Item Name" required>
                        <input type="number" name="price" placeholder="Price" step="0.01" required>
                        <button type="submit" class="btn btn-primary" style="width: 100%;">Add Item</button>
                    </form>''' if categories_options else '<p class="empty-message">Add a category first</p>'}
                </div>
            </div>

            <h2 class="section-title">Manage Items</h2>
            {items_html if items_html else '<p class="empty-message">No items yet</p>'}
        </div>

        <aside class="sidebar-updates">
            <div class="sidebar-title">📋 Recent Updates</div>
            <div>{updates_html if updates_html else '<p class="empty-message">No updates</p>'}</div>
        </aside>
    </div>
    '''

    return get_base_html("Vendor Dashboard - FoodHub", content, authenticated=True, role='vendor')


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    session_id = request.cookies.get("session_id")
    session = sessions_db.get(session_id) if session_id else None

    content = '''
    <h2 class="section-title">Contact Us</h2>
    <p style="color: #666; margin-bottom: 12px;">Meet the Team</p>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-bottom: 18px;">
        <div class="management-card" style="min-height:120px; display:flex; flex-direction:column; justify-content:center; align-items:center;">
            <img src="/static/creator1.png" alt="Creator 1" style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; margin-bottom: 8px;">
            <strong>Calubayan</strong>
            <div style="color:#999; margin-top:8px;">Alec Christian</div>
        </div>
        <div class="management-card" style="min-height:120px; display:flex; flex-direction:column; justify-content:center; align-items:center;">
            <img src="/static/creator2.png" alt="Creator 2" style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; margin-bottom: 8px;">
            <strong>De Castro</strong>
            <div style="color:#999; margin-top:8px;">Joshua Gabriel</div>
        </div>
        <div class="management-card" style="min-height:120px; display:flex; flex-direction:column; justify-content:center; align-items:center;">
            <img src="/static/creator3.jpg" alt="Creator 3" style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; margin-bottom: 8px;">
            <strong>Gan</strong>
            <div style="color:#999; margin-top:8px;">Ashley Jae</div>
        </div>
        <div class="management-card" style="min-height:120px; display:flex; flex-direction:column; justify-content:center; align-items:center;">
            <img src="/static/creator4.png" alt="Creator 4" style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; margin-bottom: 8px;">
            <strong>Ramilo</strong>
            <div style="color:#999; margin-top:8px;">Jancen</div>
        </div>
    </div>

    <div style="background: #ffffff; padding:12px; border-radius:10px; border:1px solid rgba(0,0,0,0.04);">
        <h3 style="margin-top:0;">Contact Emails</h3>
        <ul style="margin:0; padding-left:18px; color:#333;">
            <li><a href="mailto:23-09270@g.batstate-u.edu.ph">23-09270@g.batstate-u.edu.ph</a></li>
            <li><a href="mailto:23-09409@g.batstate-u.edu.ph">23-09409@g.batstate-u.edu.ph</a></li>
            <li><a href="mailto:23-02107@g.batstate-u.edu.ph">23-02107@g.batstate-u.edu.ph</a></li>
            <li><a href="mailto:23-04949@g.batstate-u.edu.ph">23-04949@g.batstate-u.edu.ph</a></li>
        </ul>
    </div>
    '''

    return get_base_html("Contact Us - FoodHub", content, authenticated=bool(session), role=session.get('role') if session else None)


@app.post("/update-status", response_class=HTMLResponse)
async def update_status(request: Request, status: str = Form(...)):
    session_id = request.cookies.get("session_id")
    if not session_id or session_id not in sessions_db:
        return RedirectResponse(url="/login", status_code=302)

    session = sessions_db.get(session_id, {})
    shop = shops.get(session.get('current_shop'))

    if shop and status in ['Open', 'Closed', 'Preparing'] and shop.status != status:
        shop.status = status
        shop.recent_updates.enqueue(f"Shop status changed to {status}")

    return RedirectResponse(url="/dashboard", status_code=302)


@app.post("/add-category", response_class=HTMLResponse)
async def add_category(request: Request, category_name: str = Form(...)):
    session_id = request.cookies.get("session_id")
    if not session_id or session_id not in sessions_db:
        return RedirectResponse(url="/login", status_code=302)

    session = sessions_db.get(session_id, {})
    shop = shops.get(session.get('current_shop'))

    if shop and category_name.strip():
        if category_name.strip().lower() in shop.menu_tree.children:
            session['error'] = f"Category '{category_name.strip()}' already exists."
        else:
            shop.add_category(category_name.strip())
            session['error'] = None

    return RedirectResponse(url="/dashboard", status_code=302)


@app.post("/add-item", response_class=HTMLResponse)
async def add_item(request: Request, category: str = Form(...), item_id: str = Form(...), item_name: str = Form(...),
                   price: str = Form(...)):
    session_id = request.cookies.get("session_id")
    if not session_id or session_id not in sessions_db:
        return RedirectResponse(url="/login", status_code=302)

    session = sessions_db.get(session_id, {})
    shop = shops.get(session.get('current_shop'))

    if shop and item_id.strip() and item_name.strip():
        try:
            if category.lower() not in shop.menu_tree.children:
                shop.menu_tree.add_child(category)
                shop.recent_updates.enqueue(f"Category '{category}' added (auto-created for item)")

            _, found = shop.find_item(item_id.strip())
            if found:
                session['error'] = f"Item ID '{item_id.strip()}' already exists."
            else:
                shop.add_item(category, item_id.strip(), item_name.strip(), float(price))
                session['error'] = None
        except ValueError:
            session['error'] = "Invalid price format. Please enter a valid number."
        except Exception as e:
            session['error'] = f"Failed to add item: {str(e)}"

    return RedirectResponse(url="/dashboard", status_code=302)


@app.post("/remove-item", response_class=HTMLResponse)
async def remove_item(request: Request, category: str = Form(...), item_id: str = Form(...)):
    session_id = request.cookies.get("session_id")
    if not session_id or session_id not in sessions_db:
        return RedirectResponse(url="/login", status_code=302)

    session = sessions_db.get(session_id, {})
    shop = shops.get(session.get('current_shop'))

    if shop:
        removed = shop.remove_item(category, item_id)
        if removed:
            pass

    return RedirectResponse(url="/dashboard", status_code=302)


@app.post("/toggle-availability", response_class=HTMLResponse)
async def toggle_availability(request: Request, category: str = Form(...), item_id: str = Form(...)):
    session_id = request.cookies.get("session_id")
    if not session_id or session_id not in sessions_db:
        return RedirectResponse(url="/login", status_code=302)

    session = sessions_db.get(session_id, {})
    shop = shops.get(session.get('current_shop'))

    if shop:
        _, item = shop.find_item(item_id)
        if item:
            shop.toggle_availability(category, item_id, not item.available)
            pass

    return RedirectResponse(url="/dashboard", status_code=302)


@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    response = RedirectResponse(url="/login", status_code=302)
    session_id = request.cookies.get("session_id")
    if session_id and session_id in sessions_db:
        del sessions_db[session_id]
    response.delete_cookie("session_id")
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
