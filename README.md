# Ansible Role: Workstation (⌐■_■)

> Because manually setting up your workstation is so 1997... (my birth year btw 👶)

An Ansible role that transforms your boring default Linux installation into my personal, fully-armed and operational DevOps battle station! (╯°□°)╯︵ ┻━┻

## Description ʕ •ᴥ•ʔ

## Requirements (°ロ°)☝

- [ ] Ansible 2.9 or higher (we're living in the future!)
- [ ] Root access or sudo privileges (with great power comes great responsibility)
- [ ] A terminal and a dream ✨
- [ ] Your favorite mechanical keyboard
- [ ] Lots of ☕

## Dependencies ⛓️

Add this to your `requirements.yml`:

```yaml
roles:
  - src: HTTPS_URL_TO_THIS_REPO
    name: ansible-role-workstation
    version: master
```

## Usage ᕦ(ò_óˇ)ᕤ

1. Add this role to your dependencies (see Dependencies section above)
2. Install it like a boss:
```bash
ansible-galaxy install -r requirements.yml
```
3. Add the role to your playbook's `meta/main.yml`:
```yaml
dependencies:
  - role: ansible-role-workstation
```
4. Run the playbook:
```bash
ansible-playbook your-playbook.yml
```
5. Watch your workstation transform into my battle-tested DevOps environment! (｀-´)>

## License 📜

MIT - Because sharing is caring! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧

## Author Information 👨‍💻

Crafted with ❤️ and definitely too much ☕ by Foxy Simon

\```
                     _____
                   .'     '.
                  /         \
                 |  ⌐■_■   |
                 |         |
                  \       /
                   '.___.'
\```

Happy automating! (▀̿Ĺ̯▀̿ ̿)
