import streamlit as st

def main():
    st.title("Lista de Compras")

    # Inicializar a lista de compras na sessão
    if 'compras' not in st.session_state:
        st.session_state.compras = []

    # Campo de entrada para adicionar item
    item = st.text_input("Adicionar item:", "")
    if st.button("Adicionar"):
        if item:
            st.session_state.compras.append(item)
            st.success(f'Item "{item}" adicionado!')
        else:
            st.warning("Digite um item para adicionar!")

    # Exibir lista de compras
    st.subheader("Itens na lista:")
    if st.session_state.compras:
        for i, compra in enumerate(st.session_state.compras):
            col1, col2 = st.columns([4, 1])
            col1.write(f"{i + 1}. {compra}")
            if col2.button("Remover", key=f"remover_{i}"):
                st.session_state.compras.pop(i)
                st.experimental_rerun()
    else:
        st.write("Nenhum item na lista.")

    # Botão para limpar a lista
    if st.button("Limpar lista"):
        st.session_state.compras = []
        st.success("Lista de compras foi limpa!")


if __name__ == "__main__":
    main()
