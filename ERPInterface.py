from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql.cursors
import matplotlib.pyplot as plt



class adminwindow():

    def GerarRelatorioDeProdutos(self):
        from reportlab.pdfgen import canvas

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from produtos')
                resultado = cursor.fetchall()
        except:
            print('erro no banco de dados')



        try:
            pdf = canvas.Canvas(f"RelatorioProdutos.pdf")
            pdf.setTitle('RelatorioProdutos')









            pdf.drawString(10, 810, "Nome")

            pdf.drawString(250, 810, "Grupo")

            pdf.drawString(500, 810, "Preço")



            altura = 780

            for linha in resultado:
                pdf.drawString(10, altura, linha['nome'])
                pdf.drawString(250, altura, linha['grupo'])
                pdf.drawString(500, altura, str(linha['preco']))
                pdf.line(10, altura-5, 700, altura-10)
                altura -= 20

            pdf.save()

            messagebox.showinfo('PDF', 'PDF criado com sucesso')
        except:
            messagebox.showinfo('PDF', 'Erro ao criar PDF')

    def limparEntry(self):
        self.nome.delete(0, END)
        self.ingredientes.delete(0, END)
        self.grupo.delete(0, END)
        self.preco.delete(0, END)

    def MostarProdutosBackEnd(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from produtos')
                resultado = cursor.fetchall()
        except:
            print('erro no banco de dados')



        self.tree.delete(*self.tree.get_children())

        i=0
        linhaV = []
        for linha in resultado:
            linhaV.append(linha['nome'])
            linhaV.append(linha['ingredientes'])
            linhaV.append(linha['grupo'])
            linhaV.append(linha['preco'])


            self.tree.insert("", END, values=linhaV, iid=linha['id'], tag='1')

            linhaV.clear()

            i+=1

    def RemoverCadastrosBackEnd(self):
        idDeletar = int(self.tree.selection()[0])

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

        except:
            print('erro ao conectar no banco de dados')

        with conexao.cursor() as cursor:
            cursor.execute('delete from produtos where id = {};'.format(idDeletar))
            conexao.commit()

        self.MostarProdutosBackEnd()

    def PesquisarPorNomeBackEnd(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        try:
            with conexao.cursor() as cursor:
                cursor.execute("select * from produtos where nome LIKE '%{}%'".format(self.pesquisar.get()))
                resultadot = cursor.fetchall()

        except:
            print('erro no banco de dados')




        self.tree.delete(*self.tree.get_children())

        i=0
        linhaV = []

        for linha in resultadot:
            linhaV.append(linha['nome'])
            linhaV.append(linha['ingredientes'])
            linhaV.append(linha['grupo'])
            linhaV.append(linha['preco'])

            self.tree.insert("", END, values=linhaV, iid=linha['id'], tag='1')

            linhaV.clear()

            i+=1

        self.pesquisar.delete(0,END)

    def PesquisarPorGrupoBackEnd(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        try:
            with conexao.cursor() as cursor:
                cursor.execute("select * from produtos where grupo LIKE '%{}%'".format(self.pesquisar.get()))
                resultadot = cursor.fetchall()

        except:
            print('erro no banco de dados')




        self.tree.delete(*self.tree.get_children())

        i=0
        linhaV = []

        for linha in resultadot:
            linhaV.append(linha['nome'])
            linhaV.append(linha['ingredientes'])
            linhaV.append(linha['grupo'])
            linhaV.append(linha['preco'])

            self.tree.insert("", END, values=linhaV, iid=linha['id'], tag='1')

            linhaV.clear()

            i+=1

        self.pesquisar.delete(0,END)

    def LimparCadastrosBackEnd(self):
        if messagebox.askokcancel('Limpar dados CUIDADO!!', 'DESEJA EXCLUIR TODOS OS DADOS DA TABELA ? NAO HÁ VOLTA!!'):

            try:
                conexao = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='Caio@lemos12',
                    db='erp',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )

            except:
                print('erro ao conectar no banco de dados')

            with conexao.cursor() as cursor:
                cursor.execute('truncate table produtos;')
                conexao.commit()

            self.MostarProdutosBackEnd()

    def CadastrarProdutoBackEnd(self):
        nome = self.nome.get()
        ingredientes = self.ingredientes.get()
        grupo = self.grupo.get()
        preco = self.preco.get()

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        with conexao.cursor() as cursor:
            cursor.execute('insert into produtos(nome, ingredientes, grupo, preco) values (%s,%s, %s, %s)', (nome, ingredientes, grupo, preco))
            conexao.commit()


        self.limparEntry()
        self.MostarProdutosBackEnd()

    def CadastrarProduto(self):
        self.cadastrar = Tk()
        self.cadastrar.resizable(True, True)
        self.cadastrar.protocol("WM_DELETE_WINDOW")
        self.cadastrar.title("Cadastrar Produtos")
        self.cadastrar['bg'] = '#524F4F'


        Label(self.cadastrar, text='Cadastre os produtos',bg='#524F4F', fg='white').grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        Label(self.cadastrar, text='Nome', bg='#524F4F', fg='white').grid(row=1, column=0, columnspan=1, padx=5, pady=5)
        self.nome = Entry(self.cadastrar)
        self.nome.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='ingredientes',bg='#524F4F', fg='white').grid(row=2, column=0, columnspan=1, padx=5, pady=5)
        self.ingredientes = Entry(self.cadastrar)
        self.ingredientes.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Grupo',bg='#524F4F', fg='white').grid(row=3, column=0, columnspan=1, padx=5, pady=5)
        self.grupo = Entry(self.cadastrar, relief='flat', highlightbackground='#524F4F')
        self.grupo.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Preço',bg='#524F4F', fg='white').grid(row=4, column=0, columnspan=1, padx=5, pady=5)
        self.preco = Entry(self.cadastrar)
        self.preco.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

        Button(self.cadastrar, text='Cadastrar', width=15, bg='gray', command=self.CadastrarProdutoBackEnd, relief='flat', highlightbackground='#524F4F').grid(row=5, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Excluir', width=15, bg='gray' , relief='flat', highlightbackground='#524F4F', command=self.RemoverCadastrosBackEnd).grid(row=5, column=1, padx=5, pady=5)
        Button(self.cadastrar, text='Atualizar', width=15, bg='gray', relief='flat', command=self.MostarProdutosBackEnd, highlightbackground='#524F4F').grid(row=6, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Limpar produtos', width=15, bg='gray', relief='flat', highlightbackground='#524F4F', command=self.LimparCadastrosBackEnd).grid(row=6, column=1, padx=5, pady=5)

        self.tree = ttk.Treeview(self.cadastrar, selectmode="browse", column=("column1", "column2", "column3", "column4" ),
                                 show='headings')

        self.tree.column("column1", width=200, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("column2", width=400, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Ingredientes')

        self.tree.column("column3", width=200, minwidth=180, stretch=NO)
        self.tree.heading('#3', text='Grupo')

        self.tree.column("column4", width=60, minwidth=180, stretch=NO)
        self.tree.heading('#4', text='Preco')

        self.tree.grid(row=0, column=4, padx=10, pady=10, columnspan=3, rowspan=6)

        self.pesquisar = Entry(self.cadastrar, width=40)
        self.pesquisar.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        Button(self.cadastrar, text='Pesquisar por nome', width=15, bg='gray', command=self.PesquisarPorNomeBackEnd,
               relief='flat', highlightbackground='#524F4F', fg='black').grid(row=9, column=0, columnspan=1, padx=5)

        Button(self.cadastrar, text='Pesquisar por grupo', width=15, bg='gray', command=self.PesquisarPorGrupoBackEnd,
               relief='flat', highlightbackground='#524F4F', fg='black').grid(row=9, column=1, columnspan=1, padx=5,
                                                                              pady=5)

        self.MostarProdutosBackEnd()

        self.cadastrar.mainloop()

    def __init__(self):
        self.admin = Tk()
        self.admin.resizable(False, False)
        self.admin.title("Painel Admnistrativo")
        self.admin.geometry("500x10")
        self.menubar = Menu(self.admin)
        self.menubar.add_separator()

        self.file_menu = Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Banco de dados")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair")
        self.menubar.add_cascade(label="Configuraçoes", menu=self.file_menu)
        self.menubar.add_separator()

        self.help_menu = Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label="Ajuda")
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Sobre")
        self.menubar.add_cascade(label="Ajuda", menu=self.help_menu)
        self.menubar.add_separator()

        self.produtos_menu = Menu(self.menubar, tearoff=0)
        self.produtos_menu.add_command(label='Cadastrar produtos', command=self.CadastrarProduto)
        self.produtos_menu.add_separator()
        self.produtos_menu.add_command(label='Gerar Relatorio', command=self.GerarRelatorioDeProdutos)
        self.menubar.add_cascade(label='Produtos', menu=self.produtos_menu)
        self.menubar.add_separator()

        self.pedidos_menu = Menu(self.menubar, tearoff=0)
        self.pedidos_menu.add_command(label='Visualizar pedidos', command=pedidoswindow)
        self.menubar.add_cascade(label='Pedidos', menu=self.pedidos_menu)
        self.menubar.add_separator()

        self.estatistica_menu = Menu(self.menubar, tearoff=0)
        self.estatistica_menu.add_command(label='Visualizar estatisticas', command=Estatisticas)
        self.menubar.add_cascade(label='Estatistica', menu=self.estatistica_menu)
        self.menubar.add_separator()


        self.admin.configure(menu=self.menubar)

        self.admin.mainloop()


class Estatisticas():
    def __init__(self):
        pass


class pedidoswindow():

    def Conectar(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')

        return conexao

    def __init__(self):
        self.pedido = Tk()
        self.pedido.title("pedidos")
        self.pedido['bg'] = '#524F4F'



        self.tree = ttk.Treeview(self.pedido, selectmode="browse",column=("column1", "column2", "column3", "column4"), show='headings', height=30)

        self.tree.column("column1", width=200, minwidth=30, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("column2", width=400, minwidth=30, stretch=NO)
        self.tree.heading('#2', text='Observações')

        self.tree.column("column3", width=200, minwidth=30, stretch=NO)
        self.tree.heading('#3', text='Grupo')

        self.tree.column("column4", width=80, minwidth=30, stretch=NO)
        self.tree.heading('#4', text='Entrega')

        self.tree.grid(row=0, column=0, padx=10, pady=10, columnspan=4 , rowspan=6)
        Button(self.pedido, text="Entregar pedido", width=15, height=10, bg='gray', relief='flat', highlightbackground='#524F4F', command=self.EntregarPedidosBackEnd).grid(row=0, column=5)
        Button(self.pedido, text = "Cancelar pedido", width=15, height=10, bg='gray', relief='flat', highlightbackground='#524F4F', command = self.CancelarPedidosBackEnd).grid(row=0, column=6)
        Button(self.pedido, text="Atualizar", width=15, height=10, bg='gray', relief='flat', highlightbackground='#524F4F', command=self.MostrarPedidosBackEnd).grid(row=1, column=5)

        self.MostrarPedidosBackEnd()
        self.pedido.mainloop()

    def MostrarPedidosBackEnd(self):

        conexao = self.Conectar()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos')
                resultado = cursor.fetchall()
        except:
            print('erro no banco de dados')

        self.tree.delete(*self.tree.get_children())


        linhaV = []
        for linha in resultado:
            linhaV.append(linha['nome'])
            linhaV.append(linha['observacoes'])
            linhaV.append(linha['grupo'])
            linhaV.append(linha['localEntrega'])

            self.tree.insert("", END, values=linhaV, iid=linha['id'], tag='1')

            linhaV.clear()

        conexao.close()

    def CancelarPedidosBackEnd(self):
        idDeletar = int(self.tree.selection()[0])
        print(idDeletar)


        conexao = self.Conectar()

        with conexao.cursor() as cursor:
            cursor.execute('delete from pedidos where id = {};'.format(idDeletar))
            conexao.commit()

        conexao.close()
        self.MostrarPedidosBackEnd()

    def EntregarPedidosBackEnd(self):

        idTree = int(self.tree.selection()[0])
        conexao = self.Conectar()

        try:
            with conexao.cursor() as cursor:
                cursor.execute("select * from pedidos where id LIKE '%{}%'".format(idTree))
                resultadoq = cursor.fetchall()

        except:
            print('erro no banco de dados')

        print(resultadoq)



        with conexao.cursor() as cursor:
            cursor.execute('insert into caixa (mesa, nome, preco) values (%s,%s, %s)', (int(resultadoq['localEntrega']), resultadoq['nome'], resultadoq['preco']))
            conexao.commit()



class mainwindow():

    def VerificaLogin(self):
        autenticado = False
        usuarioMaster = False

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar no banco de dados')

        usuario = self.usuario.get()
        senha = self.senha.get()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultado = cursor.fetchall()
        except:
            print('erro no banco de dados')

        for linha in resultado:
            if usuario == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False

        if not autenticado:
            messagebox.showinfo('Login', 'Email ou senha invalido')



        if autenticado:
            self.root.destroy()
            if usuarioMaster:
                adminwindow()


        conexao.close()

    def Update(self):

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro')


        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultado = cursor.fetchall()
        except:
            print('erro no banco de dados')



        self.tree.delete(*self.tree.get_children())

        i=0
        linhaV = []
        for linha in resultado:
            linhaV.append(linha['id'])
            linhaV.append(linha['nome'])
            linhaV.append(linha['senha'])
            linhaV.append(linha['nivel'])



            self.tree.insert("", END, values=linhaV, iid=linha['id'], tag='1')



            linhaV.clear()

            i+=1

    def VisualizarCadastros(self):
        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar no banco de dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultado = cursor.fetchall()
        except:
            print('erro no banco de dados')

        self.VC = Toplevel()
        self.VC.resizable(False, False)
        self.VC.protocol("WM_DELETE_WINDOW")
        self.VC.title("Visualizar Cadastros")

        self.tree = ttk.Treeview(self.VC, selectmode="browse", column=("column1", "column2", "column3", "column4"), show='headings')


        self.tree.column("column1", width=40, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='ID')

        self.tree.column("column2", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Usuario')

        self.tree.column("column3", width=100, minwidth=180, stretch=NO)
        self.tree.heading('#3', text='Senha')

        self.tree.column("column4", width=40, minwidth=180, stretch=NO)
        self.tree.heading('#4', text='nivel')

        self.tree.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
        Button(self.VC, text='Limpar usuarios', command=self.Remover).grid(row=1, column=0, sticky=W + E, columnspan=2, padx=5, pady=5)
        Button(self.VC, text='Atualizar', command=self.Update).grid(row=1, column=2, sticky=W + E, columnspan=1, padx=5, pady=5)

        self.Update()

        self.VC.mainloop()

    def Remover(self):

        idDeletar = int(self.tree.selection()[0])

        try:
            conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='Caio@lemos12',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

        except:
            print('erro ao conectar no banco de dados')


        with conexao.cursor() as cursor:
            cursor.execute('delete from cadastros where id = {};'.format(idDeletar))
            conexao.commit()



        self.Update()

    def __init__(self):
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW")
        self.root.title("Login")


        Label(self.root, text='Login').grid(row=0, column=0, columnspan=2, pady=5, padx=10)

        Label(self.root, text='Usuario').grid(row=1, column=0, pady=5, padx=10 )
        self.usuario = Entry(self.root)
        self.usuario.grid(row=1, column=1, pady=5, padx=10)

        Label(self.root, text='Senha').grid(row=2, column=0, pady=5, padx=10)
        self.senha = Entry(self.root, show='*')
        self.senha.grid(row=2, column=1, pady=5, padx=10)


        Button(self.root, text='Logar', width=15, bg='green', command=self.VerificaLogin).grid(row=3, column=0, pady=5, padx=10)
        Button(self.root, text='Cadastrar', width=15, bg='orange').grid(row=3, column=1, pady=5, padx=1)

        Button(self.root, text='vizualizar cadastros', bg='white', command=self.VisualizarCadastros).grid(row=4, columnspan=2, column=0, pady=5, padx=10)



        self.root.mainloop()




try:
    mainwindow()
except:
    print('erro')