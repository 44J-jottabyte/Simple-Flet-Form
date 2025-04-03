import flet

def form_submit_function(e):
    print('form submitted!')

form_container = flet.Container (
    flet.Column([
        flet.Text("Sign Up",size=24,color='black',weight='w600'),
        flet.TextField(
            label="First Name",text_size=16,border_radius=14,
            focused_border_color='#0a85ff',color = 'black',
            cursor_color='#0a85ff',border_width=0.6,border_color='black'
        ),
        flet.TextField(
            label="Email",text_size=16,border_radius=14,
            focused_border_color='#0a85ff',color = 'black',
            cursor_color='#0a85ff',border_width=0.6,border_color='black'
        ),
        flet.TextField(
            label="Password",text_size=16,border_radius=14,
            focused_border_color='#0a85ff',color = 'black',
            cursor_color='#0a85ff',border_width=0.6,border_color='black',
            password=True,can_reveal_password=True
        ),
        flet.Button(
            "Submit",color='white',
            width=700,height=40,style=flet.ButtonStyle(
                text_style=flet.TextStyle(size=16,weight='w600'),
                bgcolor='#0a85ff'
            ),
            on_click=form_submit_function
        )
        
    ],horizontal_alignment='center',spacing=20),    
    width=400,height=400,bgcolor='white',
    border_radius=18,padding=20
)

def main(page:flet.Page):
    page.window.width = 600
    page.window.height = 500
    page.vertical_alignment='center'
    page.horizontal_alignment='center'
    page.bgcolor='#e6e6eb'
    page.add(
        form_container
    )
flet.app(main)    