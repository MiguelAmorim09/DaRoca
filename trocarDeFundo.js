<script>
    window.addEventListener('scroll', function() {
        const scrollHeight = window.scrollY;
        const breakpoint = 1002; // Altura em pixels para a troca de cor

        if (scrollHeight >= breakpoint) {
            document.body.style.backgroundColor = '#33635A'; // Nova cor de fundo
        } else {
            document.body.style.backgroundColor = '#013C31'; // Cor inicial
        }
    });
</script>