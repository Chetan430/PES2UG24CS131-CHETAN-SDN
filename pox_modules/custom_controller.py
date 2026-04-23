from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

# When switch connects
def _handle_ConnectionUp(event):
    log.info("Switch %s has connected", event.connection)

# Handle incoming packets
def _handle_PacketIn(event):
    packet = event.parsed

    if not packet.parsed:
        log.warning("Ignoring incomplete packet")
        return

    log.info("Packet received from %s", packet.src)

    # Flood packet to all ports
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Custom SDN Controller Running...")